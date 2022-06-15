from dotenv import load_dotenv
import os

load_dotenv('./deployment/env/.env.local')

SECRET_KEY = 'dw213r24rf24f'
DEBUG = True
ALLOWED_HOSTS = ['*']
