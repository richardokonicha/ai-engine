import os
import sys
import logging
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

required_variables = ['OPENAI_KEY']

for variable in required_variables:
    if variable not in os.environ:
        sys.exit(f'Missing environment variable: {variable}')

DEBUG = os.getenv('DEBUG', 'True')
PORT = os.getenv('PORT', 5001)

WEBHOOK_URL = os.getenv('WEBHOOK_URL', 'https://5001-richardokon-upgradedfcx-82z3zmfnasf.ws-eu97.gitpod.io')

DATABASE_URL = os.getenv('DATABASE_URL', "mongodb+srv://******:******@cluster0.vexqcep.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.getenv('DB_NAME', 'raznesi_bot')
WEBSITE_URL = os.getenv('WEBSITE_URL', "https://queen.fugoku.com")

OPENAI_KEY = os.getenv('OPENAI_KEY', "********")

UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', "static/")
TEMPLATE_FILE = os.getenv('TEMPLATE_FILE', "template.png")

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}




