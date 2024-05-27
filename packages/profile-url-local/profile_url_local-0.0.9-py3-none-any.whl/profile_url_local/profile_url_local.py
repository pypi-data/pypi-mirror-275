from database_mysql_local.generic_crud import GenericCRUD
from logger_local.MetaLogger import MetaLogger

from .constants_url_profile_local import UrlProfileLocalConstants


class UrlProfilesLocal(GenericCRUD, metaclass=MetaLogger, object=UrlProfileLocalConstants.OBJECT_FOR_LOGGER_CODE):

    def __init__(self):
        super().__init__(default_schema_name="profile_url", default_table_name='profile_url_table',
                         default_column_name='profile_id', default_view_table_name='profile_url_view')

    def insert(self, *, url: str, url_id: int, profile_id: int):
        profile_url_dict = {'profile_id': profile_id,
                            'url_id': url_id, 'url_old': url}
        profile_url = super().insert(data_dict=profile_url_dict)
        return profile_url

    def update(self, *, url: str, url_id: int, profile_id: int) -> int:
        profile_url_dict = {'profile_id': profile_id,
                            'url_id': url_id,
                            'url_old': url}
        updated_rows = super().update_by_id(data_dict=profile_url_dict, column_value=profile_id,
                                            order_by='start_timestamp desc', limit=1)
        return updated_rows

    def delete_by_profile_id(self, profile_id: int) -> int:
        deleted_rows = super().delete_by_column_and_value(column_value=profile_id)
        return deleted_rows

    def get_last_url_by_profile_id(self, profile_id: int) -> str:
        where_clause = f"profile_id = {profile_id}"
        order = "start_timestamp desc"
        url = super().select_one_value_by_where(
            select_clause_value="url_old", where=where_clause, order_by=order)
        return url
