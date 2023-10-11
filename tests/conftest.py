import os
import sqlite3
from pathlib import Path

import pytest

from datafirst.database import close_database, get_cursor, open_database

RESOURCES_DIRECTORY = Path(__file__).parent / "resources"
DATABASE_PATH = RESOURCES_DIRECTORY / "datafirst.sqlite"


@pytest.fixture
def cursor() -> sqlite3.Cursor:
    if not os.path.exists(DATABASE_PATH):
        raise FileNotFoundError("Database not found " + str(DATABASE_PATH))
    connection = open_database(DATABASE_PATH)
    cursor = get_cursor(connection)
    yield cursor
    close_database(connection)
