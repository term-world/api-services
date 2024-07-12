import os
import sys
import requests
from dotenv import load_dotenv
from rich.console import Console
from rich.markdown import Markdown

# Load environment variables from .env file
load_dotenv()

# Verify the environment variables
print(f"GITHUB_USER: {os.getenv('GITHUB_USER')}")
print(f"API_URL: {os.getenv('API_URL')}")
print(f"API_PORT: {os.getenv('API_PORT')}")

class Persona_Creator:

    def __init__(self, name: str = "", prompt: str = "", file: str = ""):
        self.name = name or input("Persona name (no spaces): ")
        self.prompt = prompt or input("Define persona personality: ")
        self.file = file or input("File to attach (leave blank if none): ")
        self.__create_persona()

    def __create_persona(self):
        console = Console()
        try:
            data = {
                "persona_creator": os.getenv('GITHUB_USER'),
                "persona_prompt": self.prompt,
                "persona_file_name": self.file if self.file else "none"
            }
            files = {"file_binary": open(self.file, "rb")} if self.file else {}

            response = requests.post(
                f"{os.getenv('API_URL')}:{os.getenv('API_PORT')}/v1/persona/create/{self.name}",
                data=data,
                files=files
            )

            response.raise_for_status() 
            response_data = response.json()
            console.print(Markdown(f"> Response: {response_data}"))

        except FileNotFoundError:
            console.print(Markdown(f"> The file {self.file} doesn't seem to be present at the moment..."))
        except requests.exceptions.RequestException as e:
            console.print(Markdown(f"> An error occurred: {str(e)}"))
        except Exception as e:
            console.print(Markdown(f"> An unexpected error occurred: {str(e)}"))

def cmd():
    sys.path.append(os.path.expanduser(os.getcwd()))
    Persona_Creator()
