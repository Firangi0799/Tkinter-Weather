# Weather App

This is a simple weather application built using Tkinter in Python. It allows users to get the current weather information for a specified city.

## Features

- Enter the city name in the search bar and click the search button to retrieve the weather information.
- The application displays the current time and weather details, including temperature, condition, wind speed, humidity, and pressure.
- The application uses the OpenWeatherMap API to fetch weather data.

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/Firangi0799/Weather-App.git
   ```

2. Install the required dependencies:

   ```
   pip install geopy timezonefinder requests pytz
   ```

3. Obtain the necessary API key from OpenWeatherMap by creating an account on their website.

4. Replace the placeholder API key in the code with your actual API key:

   ```python
   api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=YOUR_API_KEY"
   ```

5. Run the application:

   ```
   python weather_app.py
   ```

## Usage

1. Launch the application.
2. Enter the name of the city for which you want to retrieve the weather information.
3. Click the search button or press Enter.
4. The application will display the current time and weather details for the specified city.

## Screenshots

![Weather App Screenshot](screenshots/weather_app.png)

## Dependencies

The application relies on the following dependencies:

- Tkinter: Python's standard GUI package
- Geopy: A geocoding library to retrieve the latitude and longitude of a location
- Timezonefinder: A library to determine the timezone of a location
- Requests: A library to send HTTP requests and retrieve data from APIs
- Pytz: A library for working with time zones and dates

## Contributions

Contributions are welcome! If you have any suggestions or improvements for this weather application, please feel free to submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
