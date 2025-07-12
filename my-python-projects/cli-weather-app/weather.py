
---
---

### **File 6 of 6: `my-python-projects/cli-weather-app/weather.py`**

```python
import os
import requests
import argparse
import sys
from datetime import datetime

def get_weather(city_name, api_key):
    """
    Fetches and displays weather data for a given city using the OpenWeatherMap API.
    
    :param city_name: The name of the city.
    :param api_key: Your OpenWeatherMap API key.
    """
    # API endpoint URL
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    # Parameters for the API request
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    
    try:
        # Make the API request
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        
        # Parse the JSON response
        weather_data = response.json()
        
        # Extract relevant information
        main_weather = weather_data['weather'][0]['main']
        description = weather_data['weather'][0]['description']
        temp = weather_data['main']['temp']
        feels_like = weather_data['main']['feels_like']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        country = weather_data['sys']['country']
        city = weather_data['name']
        
        # Display the formatted weather information
        print("\n" + "="*40)
        print(f"Weather in {city}, {country}")
        print(f"Retrieved at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*40)
        print(f"  Condition: {main_weather} ({description.capitalize()})")
        print(f"  Temperature: {temp}°C")
        print(f"  Feels Like: {feels_like}°C")
        print(f"  Humidity: {humidity}%")
        print(f"  Wind Speed: {wind_speed} m/s")
        print("="*40 + "\n")

    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            print(f"Error: City '{city_name}' not found. Please check the spelling.")
        elif response.status_code == 401:
            print("Error: Invalid API key. Please check your OPENWEATHER_API_KEY environment variable.")
        else:
            print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Error connecting to the weather service: {req_err}")
    except KeyError:
        print("Error: Could not parse weather data. The API response format may have changed.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Check for API Key from environment variable
    api_key = os.getenv('OPENWEATHER_API_KEY')
    if not api_key:
        print("Error: OPENWEATHER_API_KEY environment variable not set.")
        print("Please get a free API key from https://openweathermap.org/ and set the environment variable.")
        sys.exit(1) # Exit the script with an error code

    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Get the current weather for a specific city.")
    parser.add_argument('city', type=str, help="The name of the city you want the weather for.")
    
    args = parser.parse_args()
    
    get_weather(args.city, api_key)
