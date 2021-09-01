import sqlite3
from pathlib import Path

DATABASE_FILE = 'database.sqlite'
SCHEMA_FILE = 'schema.sql'

app_path = Path(__file__).parent
database_path = app_path / 'db' / DATABASE_FILE
schema_path = app_path / 'db' / SCHEMA_FILE

if database_path.exists():
    database_path.unlink()

db = sqlite3.connect(database_path, check_same_thread=False)
with open(schema_path, 'r', encoding='utf8') as schema:
    db.executescript(schema.read())
