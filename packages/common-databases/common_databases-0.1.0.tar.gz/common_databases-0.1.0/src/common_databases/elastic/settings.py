from typing import Optional
from pydantic_settings import BaseSettings


class ElasticSettings(BaseSettings):
    ELASTIC_HOSTS: Optional[str] = None
    ELASTIC_USER: Optional[str] = None
    ELASTIC_PASSWORD: Optional[str] = None
    ELASTIC_CA_CERTS: Optional[str] = None
    ELASTIC_API_KEY: Optional[str] = None
    ELASTIC_CLOUD_ID: Optional[str] = None