import os
import pytest
import yaml
from load_secrets import load_secrets


@pytest.fixture
def secrets_file(tmp_path):
    secrets = {
        "SECRET_KEY": "mysecretkey",
        "DATABASE_URL": "postgres://user:password@localhost:5432/dbname",
    }
    file_path = tmp_path / "secrets.yaml"
    with open(file_path, "w") as file:
        yaml.dump(secrets, file)
    return file_path


def test_load_secrets(secrets_file):
    load_secrets(str(secrets_file))

    assert os.environ["SECRET_KEY"] == "mysecretkey"
    assert (
        os.environ["DATABASE_URL"] == "postgres://user:password@localhost:5432/dbname"
    )


def test_load_secrets_overwrites_existing_env_vars(secrets_file):
    os.environ["SECRET_KEY"] = "oldvalue"
    load_secrets(str(secrets_file))

    assert os.environ["SECRET_KEY"] == "mysecretkey"
