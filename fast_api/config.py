import os

DATABASE = {
    "provider": os.environ.get("FASTAPI_DB_PROVIDER", "postgres"),
    "database": os.environ.get("POSTGRES_DBNAME", "fast_api"),
    "password": os.environ.get("POSTGRES_PASSWORD", "fast_api"),
    "user": os.environ.get("POSTGRES_USER", "fast_api"),
    "host": os.environ.get("POSTGRES_HOST", "localhost"),
}
