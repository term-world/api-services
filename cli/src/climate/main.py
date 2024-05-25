"""Provide weather report on local climate."""

import os
import requests
import arglite
import json
from rich.console import Console
from rich.table import Table

# Import and call the load_dotenv function from the dotenv module (loads environment variables from a .env file), 
from dotenv import load_dotenv
load_dotenv()

def main():
    """Display the weather report."""
    # define api_url and port variables
    api_url = os.getenv("API_URL")
    api_port = os.getenv("PORT")

    # send a get request to the API and store the response
    STATE = json.loads(
    requests.get(
        "https://cdn.githubraw.com/term-world/TNN/main/weather.json"
    ).text
    )

    # Textual output here that uses rich to format
    weather_emojis = {
        "Clear": "☀️",
        "Clouds": "☁️",
        "Rain": "🌧️",
        "Snow": "❄️",
        "Thunderstorm": "⛈️",
        "Drizzle": "🌦️",
        "Mist": "🌫️"
    }
    console = Console()
    table = Table(show_header=False, title="Meadville", title_style="bold magenta")
    table.add_column()
    table.add_column()
    data = [
        ("Weather", f"{weather_emojis.get(STATE['weather'][0]['main'], '')} {STATE['weather'][0]['main']}"),
        ("Temperature", f'{STATE["main"]["temp"]}°C'),
        ("Feels Like", f'{STATE["main"]["feels_like"]}°C'),
        ("Min Temp", f'{STATE["main"]["temp_min"]}°C'),
        ("Max Temp", f'{STATE["main"]["temp_max"]}°C'),
        ("Pressure", f'{STATE["main"]["pressure"]} hPa'),
        ("Humidity", f'{STATE["main"]["humidity"]}%'),
        ("Visibility", f'{STATE["visibility"]} m'),
        ("Wind Speed", f'{STATE["wind"]["speed"]} m/s'),
        ("Rain", f'{STATE.get("rain", {}).get("1h", "N/A")} mm'),
        ("Clouds", f'{STATE["clouds"]["all"]}%')
    ]
    for i, (label, value) in enumerate(data):
        table.add_row(label, value)
        if i < len(data) - 1:  # Don't add a line after the last row
            table.add_row()
    console.print("")
    console.print(table)
    console.print("")

if __name__ == "__main__":
    main()