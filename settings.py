from pydantic_settings import BaseSettings
from pydantic import validator


class Settings(BaseSettings):
    ENVIRONMENT: str
    APP_NAME: str
    SECRET: str

    @validator("ENVIRONMENT")
    def validate_environment(cls, value):
        valid_environments = {"dev", "test", "prod"}
        if value not in valid_environments:
            raise ValueError(
                f"Invalid environment: {value}. Must be one of {valid_environments}."
            )
        return value
