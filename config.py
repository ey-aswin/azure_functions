

import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# # Try to load .env only if python-dotenv is present (local dev)
# try:
#     from dotenv import load_dotenv
#     load_dotenv()  # Reads .env from current working directory
# except ModuleNotFoundError:
#     # In Azure, dotenv may not be present; we rely on App Settings.
#     pass

EMAIL_SENDER = os.getenv("SENDER_EMAIL")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
COSMOS_DB_CONNECTION_STRING =os.getenv("COSMOS_DB_CONNECTION_STRING")
COSMOS_DB_DATABASE_NAME = os.getenv("COSMOS_DB_DATABASE_NAME")
COSMOS_DB_CONTAINER_NAME = os.getenv("COSMOS_DB_CONTAINER_NAME") 
