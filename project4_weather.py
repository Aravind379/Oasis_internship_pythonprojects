import requests
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from io import BytesIO


API_KEY = "YOUR_API_KEY"  
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    """Fetch weather data for a given city from OpenWeatherMap API."""
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        messagebox.showerror("Error", f"Failed to fetch data:\n{err}")
        return None


def search_weather():
    """Trigger weather search when user clicks 'Search'."""
    city = city_entry.get().strip()
    if not city:
        messagebox.showwarning("Warning", "Please enter a city name!")
        return

    data = get_weather(city)
    if data and data.get("cod") == 200:
        show_weather(data)
    else:
        messagebox.showerror("Error", "City not found. Please check the spelling.")


def show_weather(data):
    """Update the GUI with weather details and icon."""
    city_name = f"{data['name']}, {data['sys']['country']}"
    temperature = f"{data['main']['temp']}°C"
    condition = data
