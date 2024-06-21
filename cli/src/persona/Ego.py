import os
import sys
import requests

class Ego:

    def __init__(self, name: str = ""):
        self.addressee = os.getenv('GITHUB_USER')
        self.archetype = ""
        is_registered = requests.get(
            f"{os.getenv('API_URL')}:{os.getenv('API_PORT')}/v1/persona/search/{name}/"
        )
        if is_registered.status_code != 200:
            print("ERROR: Persona is not registered!")
            sys.exit(1)
