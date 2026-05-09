import os
import sqlite3
required_env_vars = ["DB_URL"]
for var in required_env_vars:
    if not os.getenv(var):
        raise ValueError(f"Missing required environment variable: {var}")
DATABASE_URL = os.getenv("DB_URL", "sqlite:///:memory:")
conn = sqlite3.connect(DATABASE_URL)
cursor = conn.cursor()