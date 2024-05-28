import requests
import geocoder
from datetime import datetime
import os


def get_weather_details(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        raining = 'rain' in data
        snowing = 'snow' in data
        cloudiness = data['clouds']['all']

        return {
            'temperature': temperature,
            'humidity': humidity,
            'wind_speed': wind_speed,
            'raining': raining,
            'snowing': snowing,
            'cloudiness': cloudiness
        }
    else:
        return {'error': data.get('message', 'Error retrieving data')}


def get_location():
    location = geocoder.ip('me')
    return location


def extract_city(location):
    city = location.city
    return city


def get_current_datetime():
    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d")
    current_time = now.strftime("%H:%M:%S")
    current_day = now.strftime("%A")
    return current_date, current_time, current_day


def main(api_key=None):
    if api_key is None:
        api_key = os.getenv('WEATHER_API_KEY')
        if not api_key:
            print("API key is required.")
            return

    locate = get_location()
    city = extract_city(locate)

    current_date, current_time, current_day = get_current_datetime()

    temp = get_weather_details(city, api_key)

    if 'error' in temp:
        print(temp['error'])
        return

    print('*' * 50)
    print(f"City: {city}")
    print(f"Date: {current_date}")
    print(f"Time: {current_time}")
    print(f"Day: {current_day}")
    print(f"Temperature: {temp['temperature']}")
    print(f"Humidity: {temp['humidity']}")
    print(f"Wind Speed: {temp['wind_speed']}")
    if temp.get('raining'):
        print("It's Raining")
    elif temp.get('snowing'):
        print("It's Snowing")
    elif temp.get('cloudiness') > 0:
        print("It's Cloudy")
    else:
        print("It's Clear")


if __name__ == "__main__":
    api_key = "de4448eaf3862100f9dcb4a02c7d7c2a"
    main(api_key)
