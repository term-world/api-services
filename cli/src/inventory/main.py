import os
import sys
import base64
import pennant
import requests

from getpass import getuser
from dotenv import load_dotenv

from rich.table import Table
from rich.console import Console

load_dotenv()

def list():

    allowed = ["item_name", "item_qty", "item_bulk", "item_consumable"]

    api_request = requests.get(
        f"{os.getenv('API_URL')}:{os.getenv('API_PORT')}/v1/inventory/list",
        params = {
            "charname": getuser()
        }
    )

    table = Table(title=f"{getuser()}'s inventory")
    table.add_column("Item name")
    table.add_column("Item count")
    table.add_column("Space Occupied")
    table.add_column("Consumable")

    for item in api_request.json():
        values = [str(item[field]) for field in item if field in allowed]
        table.add_row(*values)

    Console().print(table)

def acquire():

    arguments = sys.argv
    if sys.argv[0].split("/")[-1] == "get":
        return

    filename = sys.argv[1]

    with open(filename, "r") as fh:
        data = fh.read()

    program = data

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

def drop():
    content = requests.post(
        f"{os.getenv('API_URL')}:{os.getenv('API_PORT')}/v1/inventory/drop/",
        data = {
            "item_owner": 1,
            "item_name": "Ticket",
            "item_qty": 1
        }
    )
    print(content.json())

