import os
import sqlite3
from pathlib import Path

import pytest

from datafirst.database import Database

RESOURCES_DIRECTORY = Path(__file__).parent / "resources"
DATABASE_PATH = RESOURCES_DIRECTORY / "datafirst.sqlite"


@pytest.fixture
def database() -> Database:
    if not os.path.exists(DATABASE_PATH):
        raise FileNotFoundError("Database not found " + str(DATABASE_PATH))
    db = Database(DATABASE_PATH)
    return db
