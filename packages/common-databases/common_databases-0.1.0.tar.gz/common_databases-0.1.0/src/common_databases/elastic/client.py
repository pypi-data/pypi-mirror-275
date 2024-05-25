import elasticsearch

from common_databases.settings import database_settings


NODES = database_settings.ELASTIC_HOSTS.split(",") if isinstance(database_settings.ELASTIC_HOSTS, str) else None
if database_settings.ELASTIC_PASSWORD is None and database_settings.ELASTIC_USER is None:
    BASIC_AUTH = None
else:
    BASIC_AUTH = (database_settings.ELASTIC_USER, database_settings.ELASTIC_PASSWORD)


client = elasticsearch.Elasticsearch(
    hosts=NODES,
    cloud_id=database_settings.ELASTIC_CLOUD_ID,
    basic_auth=BASIC_AUTH,
    ca_certs=database_settings.ELASTIC_CA_CERTS,
    api_key=database_settings.ELASTIC_API_KEY,
)