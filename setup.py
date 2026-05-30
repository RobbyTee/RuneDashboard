from getpass import getpass
from pathlib import Path

from dotenv import set_key

from database.database import test_database_connection

ENV_FILE = Path(".env")

DEFAULT_ENV_FILE = """DB_HOST = ""
DB_PORT = ""
DB_NAME = ""
DB_USER = ""
DB_PASSWORD = ""
"""


def create_env_file() -> None:
    if not ENV_FILE.exists():
        ENV_FILE.write_text(DEFAULT_ENV_FILE)


def capture_database_settings() -> dict:
    print("Please fill in the following information about your database.")

    return {
        "DB_HOST": input("  Hostname: "),
        "DB_PORT": input("  Port number (default=5432): ") or "5432",
        "DB_USER": input("  Username: "),
        "DB_PASSWORD": getpass("  Password: "),
        "DB_NAME": input("  Database name: "),
    }


def write_user_settings_to_env(settings: dict) -> None:
    for key, value in settings.items():
        if not value:
            continue
        set_key(str(ENV_FILE), key, value)


def setup() -> None:
    create_env_file()

    database_settings = capture_database_settings()

    write_user_settings_to_env(database_settings)

    print("\nConfiguration saved to .env")

    test_database_connection()


if __name__ == "__main__":
    setup()
