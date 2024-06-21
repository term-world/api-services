import os
import sys
import requests

from rich.console import Console
from rich.markdown import Markdown
from dotenv import load_dotenv

load_dotenv()

class Ego:

    def __init__(self, name: str = ""):
        self.addressee = os.getenv('GITHUB_USER')
        self.archetype = name
        self.chatterbox = False
        is_registered = requests.get(
            f"{os.getenv('API_URL')}:{os.getenv('API_PORT')}/v1/persona/search/{name}"
        )
        if is_registered.status_code == 200:
            self.behave()
        print(is_registered.status_code)

    def __send_message(self, console, msg: str = ""):
        content = requests.post(
            f"{os.getenv('API_URL')}:{os.getenv('API_PORT')}/v1/persona/generate/{self.archetype}",
            data = {
                "charname": "dluman",
                "message": msg
            },
            stream = True
        )
        output = "> "
        for chunk in content.iter_lines(decode_unicode = True):
            if chunk:
                output = f"{output}{chunk}"
        console.print(Markdown(output))

    def behave(self):
        console = Console()
        if self.chatterbox:
            self.__send_message(console, "")
        while True:
            msg = input("> ")
            self.__send_message(console, msg)
