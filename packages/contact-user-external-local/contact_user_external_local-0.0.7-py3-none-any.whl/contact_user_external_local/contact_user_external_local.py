from database_mysql_local.generic_mapping import GenericMapping
from logger_local.MetaLogger import MetaLogger
from user_context_remote.user_context import UserContext
from user_external_local.user_externals_local import UserExternalsLocal

from .contact_user_external_local_constants import CONTACT_USER_EXTERNAL_PYTHON_PACKAGE_CODE_LOGGER_OBJECT

DEFAULT_SCHEMA_NAME = 'contact_user_external'
DEFAULT_ENTITY_NAME1 = 'contact'
DEFAULT_ENTITY_NAME2 = 'user_external'
DEFAULT_ID_COLUMN_NAME = 'contact_user_external_id'
DEFAULT_TABLE_NAME = 'contact_user_external_table'
DEFAULT_VIEW_TABLE_NAME = 'contact_user_external_view'
DEFAULT_SYSTEM_ID = 6

user_context = UserContext()


class ContactUserExternalLocal(GenericMapping, metaclass=MetaLogger,
                               object=CONTACT_USER_EXTERNAL_PYTHON_PACKAGE_CODE_LOGGER_OBJECT):
    def __init__(self, system_id: int = DEFAULT_SYSTEM_ID, is_test_data: bool = False):

        GenericMapping.__init__(self, default_schema_name=DEFAULT_SCHEMA_NAME,
                                default_entity_name1=DEFAULT_ENTITY_NAME1,
                                default_entity_name2=DEFAULT_ENTITY_NAME2,
                                default_column_name=DEFAULT_ID_COLUMN_NAME,
                                default_table_name=DEFAULT_TABLE_NAME,
                                default_view_table_name=DEFAULT_VIEW_TABLE_NAME,
                                is_test_data=is_test_data)
        self.user_externals = UserExternalsLocal(is_test_data=is_test_data)
        self.system_id = system_id

    def insert_contact_and_link_to_existing_or_new_user_external(
            # TODO change dict -> dict[Contact] (not used)
            # TODO change str -> EmailAddress
            self, *, contact_dict: dict, contact_email_address: str,
            contact_id: int, system_id: int = None, user_external_dict: dict = None) -> int or None:
        """
        Insert contact and link to existing or new user_external
        :param contact_dict: contact dict
        :param contact_id: contact id
        :param contact_email_address: contact email address
        :param system_id: system id
        :param user_external_dict: user_external dict
        :return: contact_user-external_id
        """
        profile_id = user_context.get_effective_profile_id()
        system_id = system_id or self.system_id
        access_token = expiry = refresh_token = None
        if user_external_dict:
            # username = user_external_dict.get("username", contact_email_address)
            profile_id = user_external_dict.get("profile_id", profile_id)
            system_id = user_external_dict.get("system_id", system_id)
            access_token = user_external_dict.get("access_token")
            expiry = user_external_dict.get("expiry")
            refresh_token = user_external_dict.get("refresh_token")
            # oauth_token = user_external_dict.get("oauth_token")
            # oauth_token_secret = user_external_dict.get("oauth_token_secret")
            # oauth_callback_confirmed = user_external_dict.get("oauth_callback_confirmed")
            # environment_id_old = user_external_dict.get("environment_id_old")

        user_external_id = self.user_externals.select_one_value_by_where(
            select_clause_value="user_external_id", where="username=%s AND system_id=%s",
            # TODO allow to send to order_by also order_by_array with two items "start_timestamp" and DESC enum- This way we can move to other non SQL databases
            params=(contact_email_address, system_id), order_by="start_timestamp DESC")

        if not user_external_id:
            if not access_token:
                self.logger.warning("access_token is None")
                return
            # create new user_external and add it to user_external_table
            self.logger.info("user_external_id is None, creating new user_external")
            # TODO: when ready, use the minsert method that returns the id
            self.user_externals.insert_or_update_user_external_access_token(
                username=contact_email_address, profile_id=profile_id, system_id=system_id,
                access_token=access_token, expiry=expiry, refresh_token=refresh_token)
            # TODO: when ready, use the minsert method that returns the id
            user_external_id = self.user_externals.select_one_value_by_where(
                select_clause_value="user_external_id",
                where="username=%s AND system_id=%s",
                params=(contact_email_address, system_id),
                order_by="start_timestamp DESC")
            if not user_external_id:
                raise Exception("user_external_id not found")
            contact_user_external_id = self.insert_mapping(
                entity_name1=self.default_entity_name1, entity_name2=self.default_entity_name2,
                entity_id1=contact_id, entity_id2=user_external_id,
                ignore_duplicate=True)
        else:
            # link to existing user_external
            self.logger.info("user_external_id is not None, linking to existing user_external")
            # TODO contact_user_external_mapping_result_tuple
            mapping_tuple = self.select_multi_mapping_tuple_by_id(
                entity_name1=self.default_entity_name1, entity_name2=self.default_entity_name2,
                entity_id1=contact_id, entity_id2=user_external_id)
            if not mapping_tuple:
                self.logger.info("mapping_tuple is None, creating new mapping")
                contact_user_external_id = self.insert_mapping(
                    entity_name1=self.default_entity_name1, entity_name2=self.default_entity_name2,
                    entity_id1=contact_id, entity_id2=user_external_id,
                    ignore_duplicate=True)
            else:
                self.logger.info("mapping_tuple is not None")
                contact_user_external_id = mapping_tuple[0]

        return contact_user_external_id
