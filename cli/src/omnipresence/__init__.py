import os
import requests

from getpass import getuser
from dotenv import load_dotenv()
load_dotenv()

def main():
    response = requests.post(
        os.getenv('API_URL'),
        data = {
            "username": getuser(),
            "charname": getuser(),
            "working_dir": os.getcwd()
        }
    )

