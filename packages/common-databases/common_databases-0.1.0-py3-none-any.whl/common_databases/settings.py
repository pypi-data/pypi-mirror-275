from pydantic_settings import BaseSettings

from common_databases.elastic.settings import ElasticSettings
from common_databases.postgres.settings import PostgresSettings


class DatabaseSettings(BaseSettings, ElasticSettings, PostgresSettings):
    pass


database_settings = DatabaseSettings(_env_file=".env")