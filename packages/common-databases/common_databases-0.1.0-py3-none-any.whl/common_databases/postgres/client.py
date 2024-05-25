from sqlalchemy.ext.asyncio import create_async_engine

from common_databases.settings import database_settings


CREDS = ""
if database_settings.POSTGRES_USER and database_settings.POSTGRES_PASSWORD:
    CREDS = f"{database_settings.POSTGRES_USER}:{database_settings.POSTGRES_PASSWORD}@"
DB = "" if database_settings.POSTGRES_DB_NAME is None else f"/{database_settings.POSTGRES_DB_NAME}"
URI = f"postgresql+psycopg2://{CREDS}{database_settings.POSTGRES_HOST}:{database_settings.POSTGRES_PORT}{DB}"

client = create_async_engine(url=URI)