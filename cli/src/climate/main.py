"""Provide a weather report on local climate."""

import os
import requests
import json
from rich.console import Console
from rich.table import Table

# Import and call the load_dotenv function from the dotenv module (loads environment variables from a .env file)
from dotenv import load_dotenv
load_dotenv()

def main():
    """Display the weather report."""
    # Define api_url and port variables
    api_port = os.getenv("PORT")
    api_url = os.getenv("API_URL")

    # If the API URL is localhost, append the port number
    if "127.0.0.1" in api_url:
        api_url = f"{api_url}:{api_port}"
    
    # https://api.theterm.world/v1/climate/all and 8000 //// http://127.0.0.1 and 443 --> these are the 2 locations for running the api
    # Sends a get request to the url and stores the response
    STATE = json.loads(
        requests.get(
            api_url
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
    # data = [("Windy", "Yes" if STATE['wind']['windy'] else "No"), ("Wind Speed", f'{STATE["wind"]["windspeed"]} m/s'), ("Sun", "Yes" if STATE['sun'] else "No")]
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