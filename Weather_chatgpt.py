import requests
import tkinter as tk

# Define the API endpoint and API key
API_ENDPOINT = "https://api.weatherapi.com/v1/current.json"
API_KEY = "ce1cbdf3890c4a7c8cb113744231604"

# Define a function to make the API request and return the weather data
def get_weather_data(city):
    params = {"key": API_KEY, "q": city, "units": "metric"}
    response = requests.get(API_ENDPOINT, params=params)
    data = response.json()
    return data

# Create a Tkinter window
window = tk.Tk()
window.title("Weather App")

# Create the city label and entry widgets
city_label = tk.Label(window, text="Enter City Name:")
city_label.pack()

city_entry = tk.Entry(window)
city_entry.pack()

# Create the weather label widget
weather_label = tk.Label(window, text="")
weather_label.pack()

# Define a function to handle user input
def get_weather():
    city = city_entry.get()
    weather_data = get_weather_data(city)
    if "error" not in weather_data:
        temp = weather_data["current"]["temp_c"]
        description = weather_data["current"]["condition"]["text"]
        humidity = weather_data['current']['humidity']
        pressure = weather_data['current']['pressure_mb']
        wind = weather_data['current']['wind_kph']
        weather_label.config(text=f"Weather:\n{temp}°C\n{description}\n Humidity: {humidity}\n Pressure: {pressure}\n Wind: {wind}")
    else:
        weather_label.config(text="City not found.")

# Create the button widget
button = tk.Button(window, text="Get Weather", command=get_weather)
button.pack()

# Start the main loop
window.mainloop()
