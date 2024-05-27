# Whatnow

Whatnow is a Python module that retrieves the current weather details for your location. It uses the OpenWeatherMap API to fetch weather data and geocoder to determine your current location based on your IP address.

## Features

- Get current temperature, humidity, wind speed, and cloudiness
- Check if it is raining or snowing
- Display the current date, time, and day of the week

## Installation

To use this module, you need to install the required dependencies:

```bash
pip install requests geocoder
```
# Usage

Get an API Key from OpenWeatherMap 

    Sign up at OpenWeatherMap to get your free API key.

Update the API Key in the Script

    Replace the placeholder API key in the script with your actual API key:
    python

api_key = "your_actual_api_key_here"

Run the Script

Execute the script to get the current weather details:

bash

    python whatnow.py

Example Output

markdown

**************************************************
City: Your City
Date: 2023-05-26
Time: 14:23:45
Day: Friday
Temperature: 25.0°C
Humidity: 60%
Wind Speed: 5.0 m/s
It's Clear

# Functions
get_weather_details(city_name, api_key)

Fetches weather details for the specified city using the OpenWeatherMap API.

    Parameters:
        city_name (str): The name of the city to fetch weather details for.
        api_key (str): Your OpenWeatherMap API key.

    Returns:
        A dictionary with weather details such as temperature, humidity, wind speed, cloudiness, and whether it is raining or snowing.

get_location()

Determines the current location based on the IP address.

    Returns:
        A geocoder location object.

extract_city(location)

Extracts the city name from a geocoder location object.

    Parameters:
        location (geocoder object): The location object to extract the city from.

    Returns:
        The name of the city (str).

get_current_datetime()

Gets the current date, time, and day of the week.

    Returns:
        A tuple containing the current date (str), time (str), and day (str).

main()

Main function that orchestrates the retrieval and display of weather details.
License

This project is licensed under the MIT License. See the LICENSE file for details.
Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
Author

Deepak Kumar Upadhayay - dku3132@gmail.com
Acknowledgments

    OpenWeatherMap for providing the weather API.
    Geocoder for providing the location API.

 