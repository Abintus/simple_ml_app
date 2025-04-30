import os
import argparse
from dotenv import load_dotenv
from settings import Settings
from load_secrets import load_secrets


def export_envs(environment: str = "dev") -> None:
    env_files = {
        "dev": ".env.dev",
        "test": ".env.test",
        "prod": ".env.prod",
    }

    if environment not in env_files:
        raise ValueError(
            f"Invalid environment: {environment}. Must be one of {list(env_files.keys())}."
        )

    env_file = env_files[environment]
    if os.path.exists(env_file):
        load_dotenv(dotenv_path=env_file)
    else:
        raise FileNotFoundError(
            f"The .env file for the '{environment}' environment does not exist: {env_file}"
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables from specified.env file."
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="dev",
        help="The environment to load (dev, test, prod)",
    )
    args = parser.parse_args()

    load_secrets("secrets.yaml")

    export_envs(args.environment)

    settings = Settings()

    print("APP_NAME: ", settings.APP_NAME)
    print("ENVIRONMENT: ", settings.ENVIRONMENT)
    print("SECRET:", settings.SECRET)
