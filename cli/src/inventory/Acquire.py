import sys
import base64

import .Instance
from .Exceptions import *

from importlib import import_module

class Acquisition:

    def __init__(self):
        for filename in sys.argv[1:]:
            instance = Instance(filename)

    def __validate_file(self, filename: str = "") -> dict:
        status = {"name: "", "valid": True}
        try:
            status["name"] = filename.split(".")[0]
            obj = import_module(filename)
            getattr(obj, staus["name"])().use
        except Exception as e:
            status["valid"] = False
        return status

    def __read_file(self, filename: str = "") -> str:
        with open(filename, "r") as fh:
            return fh.read()

    def __get_item_properties(self): -> dict:
        pass

    def __transmit_to_api(self)- > None:
        pass

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

def cmd():
    # Validate correct use of function
    try:
        if sys.argv[0].split("/")[-1] != "get":
            raise InvalidCommandException(
                "Cannot call Acqusition directly!"
            )
    except InvalidCommandException as e:
        print(e)
        sys.exit(1)
    try:
        if len(sys.argv) < 2:
            raise InvalidArgumentsException(
                "At least one item name required!"
            )
    except InvalidArgumentsException as e:
        print(e)
        sys.exit(1)
    # Failing any issues, start Acquisition
    Acquisition()
