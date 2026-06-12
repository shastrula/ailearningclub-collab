import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DEBUG = os.getenv('DEBUG', 'false').lower() == 'true'
    MODEL_PATH = os.getenv('MODEL_PATH', 'model.pkl')
    BATCH_SIZE = int(os.getenv('BATCH_SIZE', '32'))
    API_KEY = os.getenv('API_KEY')  # From .env