import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()
project_root = Path(__file__).parent
file_path = project_root / 'ajax_app.apk'
email = os.getenv('LOGIN')
password = os.getenv('PASSWORD')

valid_credentials = (email, password)
