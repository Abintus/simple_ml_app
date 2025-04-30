import yaml
import os


def load_secrets(file_path: str):
    with open(file_path, "r") as file:
        secrets = yaml.safe_load(file)
    for key, value in secrets.items():
        os.environ[key] = value
        print(f"Loaded secret: {key} = {value}")
