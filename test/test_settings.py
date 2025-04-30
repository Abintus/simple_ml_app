import pytest
from pydantic import ValidationError
from settings import Settings


def test_settings_load_correctly():
    # Arrange
    valid_data = {
        "ENVIRONMENT": "dev",
        "APP_NAME": "SimpleMLApp",
        "SECRET": "supersecretkey",
    }

    # Act
    settings = Settings(**valid_data)

    # Assert
    assert settings.ENVIRONMENT == "dev"
    assert settings.APP_NAME == "SimpleMLApp"
    assert settings.SECRET == "supersecretkey"


def test_invalid_environment_raises_error():
    # Arrange
    invalid_data = {
        "ENVIRONMENT": "invalid_env",
        "APP_NAME": "SimpleMLApp",
        "SECRET": "supersecretkey",
    }

    # Act & Assert
    with pytest.raises(ValidationError) as exc_info:
        Settings(**invalid_data)

    assert "Invalid environment" in str(exc_info.value)
