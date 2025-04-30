import pytest
import os
from main import export_envs


def test_export_envs_valid_environment(monkeypatch):
    # Mock the os.path.exists function to always return True
    monkeypatch.setattr(os.path, "exists", lambda path: True)

    # Test with a valid environment
    try:
        export_envs("test")
    except Exception as e:
        pytest.fail(f"export_envs raised an exception unexpectedly: {e}")


def test_export_envs_invalid_environment():
    # Test with an invalid environment
    with pytest.raises(
        ValueError, match="Invalid environment: invalid_env. Must be one of .*"
    ):
        export_envs("invalid_env")


def test_export_envs_missing_env_file(monkeypatch):
    # Mock the os.path.exists function to always return False
    monkeypatch.setattr(os.path, "exists", lambda path: False)

    # Test with a valid environment but missing .env file
    with pytest.raises(
        FileNotFoundError,
        match="The .env file for the 'test' environment does not exist: .*",
    ):
        export_envs("test")
