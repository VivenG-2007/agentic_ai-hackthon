import os
DATABASE_URL = os.getenv("DB_URL", "sqlite:///:memory:")
API_SECRET = os.getenv("API_SECRET", "default_api_secret")
# rest of the code...