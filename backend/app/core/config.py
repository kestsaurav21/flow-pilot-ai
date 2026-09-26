import os

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg://flowpilot:flowpilot_dev_password@localhost:5432/flowpilot",
)