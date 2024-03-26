import os
from dotenv import load_dotenv

load_dotenv()

MAX_MESSAGE_LENGTH = int(os.getenv('MAX_MESSAGE_LENGTH', 10485760))