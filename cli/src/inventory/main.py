import os
import pennant
import requests

from getpass import getuser
from dotenv import load_dotenv
from arglite import parser as cliarg

load_dotenv()

def list():
    content = requests.get(
        f"{os.getenv('API_URL')}:{os.getenv('API_PORT')}/v1/inventory/list",
        params = {
            "charname": getuser()
        }
    )
    return content.json()

def acquire():
    # TODO: Make wayyyyy more dynamic
    content = requests.post(
        f"{os.getenv('API_URL')}:{os.getenv('API_PORT')}/v1/inventory/add/",
        data = {
            "item_owner": 1,
            "item_name": "Ticket",
            "item_qty": 1,
            "item_weight": 1,
            "item_bulk": 1,
            "item_consumable": True,
            "item_bytestring": base64.b64encode(bytes(program, 'utf-8'))
        }
    )
