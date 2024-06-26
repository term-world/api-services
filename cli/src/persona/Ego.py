import os
import sys
import types
import requests

from rich.console import Console
from rich.markdown import Markdown
from dotenv import load_dotenv

load_dotenv()

class Ego:

    def __init__(self, type: str = "", name: str = "", mode = "talk"):
        self.addressee = os.getenv('GITHUB_USER')
        self.archetype = type
        self.named = name or type
        self.chatterbox = False
        is_registered = requests.get(
            f"{os.getenv('API_URL')}:{os.getenv('API_PORT')}/v1/persona/search/{type}"
        )
        if is_registered.status_code == 200 and mode == "talk":
            self.behave()
            sys.exit(0)

    def __str__(self):
        reference = self.named or self.archetype
        return f"""You look at {reference}. {reference} looks back. It's awkward."""

    def __send_message(self, console, msg: str = ""):
        content = requests.post(
            f"{os.getenv('API_URL')}:{os.getenv('API_PORT')}/v1/persona/generate/{self.archetype}",
            data = {
                "charname": os.getenv('GITHUB_USER'),
                "message": msg
            },
            stream = True
        )
        # formatted = self.__fmt_blockquotes(content.text)
        console.print(Markdown(content.text))
        if msg.lower() == "goodbye":
            sys.exit(0)

    def __fmt_blockquotes(self, text: str = ""):
        paras = text.split("\n\n")
        return ''.join(["\n> " + para for para in paras])

    def behave(self):
        console = Console()
        if self.chatterbox:
            self.__send_message(console, "")
        while True:
            msg = input("> ")
            self.__send_message(console, msg)
