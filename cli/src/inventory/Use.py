import os
import sys
import types
import base64
import requests
import importlib

from dotenv import load_dotenv
from .Instance import Instance

load_dotenv()

class Usage:

    def __init__(self, item_name):
        self.item_name = item_name
        item_record = self.__search_inventory()
        if not item_record:
            print(f"ERROR: You don't seem to have any {item_name}!")
            sys.exit(1)
        self.__decode_item_file(item_record)
        self.__use_item()

    def __search_inventory(self, item_name: str = "") -> dict:
        item = requests.post(
            f"{os.getenv('API_URL')}:{os.getenv('API_PORT')}/v1/inventory/search/",
            data = {
                "charname": os.getenv('GITHUB_USER'),
                "item_name": self.item_name
            }
        )
        if item.status_code == 200:
            return item.json()
        return {}

    def __decode_item_file(self, item_record: dict = {}) -> None:
        self.source = bytes.fromhex(
            item_record['item_bytestring']
        ).decode('utf-8')

    def __use_item(self):
        mod = types.ModuleType(self.item_name)
        exec(self.source, mod.__dict__)
        getattr(mod, self.item_name)().use()
        status = requests.patch(
            f"{os.getenv('API_URL')}:{os.getenv('API_PORT')}/v1/inventory/reduce/",
            data = {
                "item_name": self.item_name,
                "item_owner": os.getenv('GITHUB_USER')
            }
        )

def cmd():
    Usage(sys.argv[1])

