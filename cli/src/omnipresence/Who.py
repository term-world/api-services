import os
import sys
import requests

from dotenv import load_dotenv

load_dotenv()

class Who:

    def __init__(self):
        self.cwd = os.getcwd()
        self.user = os.getenv('GITHUB_USER')
        user_list = self.__get_user_list()

    def __get_user_list(self):
        actives = requests.post(
            f"{os.getenv('API_URL')}:{os.getenv('API_PORT')}/v1/omnipresence/local/",
            data = {
                "cwd": self.cwd
            }
        )
        print(actives.json())

def cmd():
    Who()
