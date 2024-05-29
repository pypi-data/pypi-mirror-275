from enum import Enum

from pydantic import HttpUrl
from pydantic_settings import BaseSettings

from bigdata.models.search import Ranking


class ClerkInstanceType(str, Enum):
    DEV = "DEV"
    PROD = "PROD"


class LLMSettings(BaseSettings):
    USE_HYBRID: bool = True
    RANKING: Ranking = Ranking.STABLE


class Settings(
    BaseSettings
):  # FIXME OLD AUTH remove Clerk config when old auth is removed
    PACKAGE_NAME: str = "bigdata-client"  # The name of the python package
    BIGDATA_API_URL: HttpUrl = "https://api.bigdata.com"
    UPLOAD_API_URL: HttpUrl = "https://upload.ravenpack.com/1.0/"
    CLERK_INSTANCE_TYPE: ClerkInstanceType = ClerkInstanceType.PROD
    CLERK_FRONTEND_URL: HttpUrl = "https://clerk.bigdata.com/v1"
    LLM: LLMSettings = LLMSettings()


settings = Settings()
