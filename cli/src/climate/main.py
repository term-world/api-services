import os
import requests
import arglite

from dotenv import load_dotenv

load_dotenv()

def main():
    api_url = os.getenv("API_URL")
    api_port = os.getenv("PORT")
    state = requests.get(
        f"{api_url}:{api_port}/services/api/v1/climate"
    )
    print(state.content)
