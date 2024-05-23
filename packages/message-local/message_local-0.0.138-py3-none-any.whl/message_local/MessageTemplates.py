from functools import lru_cache

from database_mysql_local.generic_crud_ml import GenericCRUDML
from logger_local.MetaLogger import MetaLogger

from .MessageConstants import object_message
from .Recipient import Recipient

cache = {}


class MessageTemplates(GenericCRUDML, metaclass=MetaLogger, object=object_message):
    def __init__(self):
        super().__init__(default_schema_name="field", default_table_name="field_table")

    # TODO recipients means people, contacts, users, or profiles? - Let's discuss
    def get_potentials_recipients(self, criteria_dict: dict, recipients: list[Recipient] = None) -> list[dict]:
        """:return a list of potential recipients for the given criteria_dict and recipients."""
        if "get_potentials_recipients" not in cache:
            cache["get_potentials_recipients"] = {}
        cache_key = str((criteria_dict, recipients))
        if cache_key in cache["get_potentials_recipients"]:
            return cache["get_potentials_recipients"][cache_key]

        where = self.get_where_by_criteria_dict(criteria_dict)
        if recipients:
            assert all(recipient.get_profile_id() is not None for recipient in recipients)
            profile_ids_str = ",".join(str(recipient.get_profile_id()) for recipient in recipients)
            where += f" AND user.profile_id IN ({profile_ids_str})"
        query_for_potentials_recipients = f"""
            SELECT DISTINCT user_id,
                            person_id,
                            user_main_email_address,
                            user.profile_id AS profile_id,
                            profile_phone_full_number_normalized,
                            profile_preferred_lang_code
            FROM user.user_general_view AS user
                     JOIN group_profile.group_profile_view AS group_profile on group_profile.profile_id = user.profile_id
            WHERE {where}"""
        columns = ("user_id, person_id, user_main_email_address, profile_id,"
                   "profile_phone_full_number_normalized, profile_preferred_lang_code")
        self.cursor.execute(query_for_potentials_recipients)
        result = [self.convert_to_dict(row, columns) for row in self.cursor.fetchall()]
        cache["get_potentials_recipients"][cache_key] = result
        return result

    def get_where_by_criteria_dict(self, criteria_dict: dict) -> str:
        # TODO add support to user_external_id in criteria_dict
        min_age = criteria_dict.get("min_age")
        max_age = criteria_dict.get("max_age")
        gender_list_id = criteria_dict.get("gender_list_id")
        # TODO I believe this method should return the gender_ids based on gender_list_id
        # TODO I think this method should return both a merge of group_id and the group_ids from group_list_id
        group_list_id = criteria_dict.get("group_list_id")
        self.logger.info(object={"min_age": min_age, "max_age": max_age, "gender_list_id": gender_list_id,
                                 "group_list_id": group_list_id})
        # profile_id didn't receive messages from this campaign for campaign.minimal_days
        where = "TRUE "
        if min_age is not None:
            where += f" AND TIMESTAMPDIFF(YEAR, person_birthday_date, CURDATE()) >= {min_age}"
        if max_age is not None:
            where += f" AND TIMESTAMPDIFF(YEAR, person_birthday_date, CURDATE()) <= {max_age}"

        if gender_list_id is not None:
            gender_cache_key = ("gender", gender_list_id)
            if gender_cache_key not in cache:
                profile_gender_id_list = self.sql_in_list_by_entity_list_id(
                    schema_name="gender", entity_name="gender", entity_list_id=gender_list_id)
                cache[gender_cache_key] = profile_gender_id_list
            else:
                profile_gender_id_list = cache[gender_cache_key]

            where += " AND profile_gender_id " + profile_gender_id_list

        if group_list_id is not None:
            group_cache_key = ("group", group_list_id)
            if group_cache_key not in cache:
                group_id_list = self.sql_in_list_by_entity_list_id(
                    schema_name="group", entity_name="group", entity_list_id=group_list_id)
                cache[group_cache_key] = group_id_list
            else:
                group_id_list = cache[group_cache_key]
            where += " AND group_profile.group_id " + group_id_list
        return where

    # TODO How can we support multiple criteria tables i.e. criteria_table, real_estate_criteria, people_criteria ... with two levels hierarchy
    # TODO How can we support criteria_set? we potentially have criteria_set in each message_template_text_block
    # TODO: use criteria-local package
    @lru_cache
    def get_critiria_dict(self, message_template_id: int) -> dict:
        query = """
            SELECT DISTINCT min_age, max_age, gender_list_id, group_list_id
            FROM message_template.message_template_view
                     JOIN message_template.message_template_message_template_text_block_view AS message_template_message_template_text_block
                          ON message_template_message_template_text_block.message_template_id =
                             message_template_view.message_template_id
                     JOIN message_template.message_template_text_block_view AS message_template_text_block
                          ON message_template_text_block.message_template_text_block_id =
                             message_template_message_template_text_block.message_template_id
                     JOIN criteria.criteria_view AS criteria
                          ON criteria.criteria_id = message_template_text_block.criteria_id
            WHERE message_template_view.message_template_id = %s
            LIMIT 1  -- TODO: remove
          """  # noqa
        self.cursor.execute(query, (message_template_id,))

        columns = "min_age, max_age, gender_list_id, group_list_id"
        critiria_dict = self.convert_to_dict(self.cursor.fetchone(), columns)
        if not any(critiria_dict.values()):
            critiria_dict = {}  # All fields are None
        return critiria_dict

    @lru_cache
    def get_textblocks_and_attributes_by_form_id(self, form_id: int) -> list[dict]:
        """
            form_id
            form_name
            min_message_template
            max_message_template
            form_page
            form_message_seq_in_page
            form_message_template_id
            message_template_id
            message_template_name
            message_template_text_block_seq
            message_template_text_block_id
            message_template_text_block_name
            default_subject_template
            default_body_template
            message_template_text_block_ml_lang_code
            question_id
            question_title
            question_ml_lang_code
            default_question_possible_answer_id
            schema_attribute
            uischema_attribute
            question_type_id
            question_type_name
            variable_id
            variable_name
            variable_ml_title
            field_name
            message_template_text_block_is_visible
            possible_answer
        """
        query_by_form_id = """
        SELECT * FROM form.form_general_view WHERE form_id = %s
            ORDER BY form_page, form_message_seq_in_page, message_template_text_block_seq;"""
        self.cursor.execute(query_by_form_id, (form_id,))
        return [self.convert_to_dict(row, select_clause_value="*") for row in self.cursor.fetchall()]

    @lru_cache
    def get_textblocks_and_attributes_by_message_template_id(self, message_template_id: int) -> list[dict]:
        assert isinstance(message_template_id, int)  # TODO: do we want to allow None (all ids)
        query = """
SELECT 
       message_template_general.question_id AS question_id,
       message_template_general.question_type_id AS question_type_id,
       message_template_general.variable_id AS variable_id,
       message_template_general.question_is_required AS is_required,
       message_template_general.schema_attributes AS schema_attribute,
       message_template_general.uischema_attributes AS uischema_attribute,
       message_template_general.question_type_schema_attributes AS question_type_schema_attributes,
       message_template_general.question_type_uischema_attributes AS question_type_uischema_attributes,
       message_template_general.`question.title` AS question_title,
       message_template_general.question_ml_lang_code AS question_ml_lang_code,
       message_template_general.message_template_text_block_ml_lang_code AS message_template_text_block_ml_lang_code,
       message_template_general.message_template_text_block_name AS message_template_text_block_name,
       message_template_general.message_template_text_block_seq AS message_template_text_block_seq,
       message_template_general.question_type_name AS question_type_name,
       message_template_general.possible_answer AS possible_answer,
       message_template_general.message_template_text_block_is_visible AS message_template_text_block_is_visible,
       message_template_general.message_template_text_block_id,
       message_template_general.message_template_id AS message_template_id,
       message_template_general.default_question_possible_answer_id AS default_question_possible_answer_id,
       message_template_general.sms_body_template AS sms_body_template,
       message_template_general.email_subject_template AS email_subject_template,
       message_template_general.email_body_html_template AS email_body_html_template,
       message_template_general.whatsapp_body_template AS whatsapp_body_template,
       message_template_general.default_subject_template AS default_subject_template,
       message_template_general.default_body_template AS default_body_template

FROM message_template.message_template_general_view AS message_template_general
"""  # noqa

        where = f" WHERE message_template_id = {message_template_id} "
        order_by = " ORDER BY message_template_general.message_template_text_block_seq;"
        query += where + order_by

        self.cursor.execute(query)
        columns = ("question_id, question_type_id, variable_id, is_required, schema_attribute, uischema_attribute,"
                   "question_type_schema_attributes, question_type_uischema_attributes, question_title,"
                   "question_ml_lang_code, message_template_text_block_ml_lang_code, message_template_text_block_name,"
                   "message_template_text_block_seq, question_type_name, possible_answer, message_template_text_block_is_visible,"
                   "message_template_text_block_id, message_template_id, default_question_possible_answer_id, sms_body_template,"
                   "email_subject_template, email_body_html_template, whatsapp_body_template, default_subject_template,"
                   "default_body_template")
        # for inner_row in self.cursor.fetchall():
        #     text_block_dict = self.convert_to_dict(inner_row, ", ".join(columns))
        #
        #     text_block_dict["possibleAnswers"] = self._get_possible_answers(
        #         question_id=text_block_dict["questionId"])
        #     self.logger.info(object={"text_block_dict": text_block_dict})
        #     textblocks_and_attributes.append(text_block_dict)

        return [self.convert_to_dict(row, select_clause_value=columns) for row in self.cursor.fetchall()]

    # def _get_possible_answers(self, question_id: int) -> list[dict]:
    #     # TODO: get cities etc and insert as a possible answer.
    #     # We don't join this with the above query, because we want to keep the possible answers separated in a list.
    #     query = """
    #         SELECT value
    #         FROM question.question_possible_answer_table
    #                  JOIN question.question_possible_answer_ml_view AS question_possible_answer_ml
    #                       ON question_possible_answer_ml.question_possible_answer_id =
    #                          question_possible_answer_table.question_possible_answer_id
    #         WHERE question_id = %s """
    #     self.cursor.execute(query, (question_id,))
    #     # We will change action in the future.
    #     return [{"answerValue": row[0], "action": None} for row in self.cursor.fetchall()]
