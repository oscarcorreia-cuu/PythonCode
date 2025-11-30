import requests
import sys

# --- Configuration ---
# Coordinates for a sample location (e.g., London, UK)
# You can easily find the coordinates for any city using a search engine.
# Web site:  https://open-meteo.com/
# LATITUDE = 51.5074  # Latitude of the location
# LONGITUDE = 0.1278   # Longitude of the location
# CITY_NAME = "Kamapla Uganda"

LATITUDE = 0  # Latitude of the location
LONGITUDE = 0   # Longitude of the location
CITY_NAME = "Kamapla Uganda"


# Open-Meteo API URL (Free and no API Key required for basic usage)
BASE_URL = "https://api.open-meteo.com/v1/forecast"
# BASE_URL = "https://api.open-meteo.com/v1/forecastxyz"

# Parameters we want to request from the API
# We ask for the current weather (current_weather=true)
# and a few hourly parameters (temperature, relative humidity, wind speed).
PARAMS = {
    "latitude": LATITUDE,
    "longitude": LONGITUDE,
    "current_weather": "true",
    "hourly": "temperature_2m,relative_humidity_2m,wind_speed_10m",
    "timezone": "auto",
    "forecast_days": 1
}

def get_current_weather(city_name, url, params):
    """
    Fetches and displays current weather data for the configured location.

    Args:
        city_name (str): The name of the city for display purposes.
        url (str): The base URL of the weather API.
        params (dict): Dictionary of query parameters including coordinates.
    """
    print(f"--- Fetching Weather for {city_name} ---")

    try:
        # Make the GET request to the API endpoint
        response = requests.get(url, params=params)
        
        # Check for HTTP errors (like 404 or 500)
        response.raise_for_status()

        # Parse the JSON response body into a Python dictionary
        data = response.json()

        # Extract relevant weather data from the nested dictionary
        current = data.get('current_weather')
        
        if not current:
            print("Error: Could not find current weather data in the response.")
            return

        # Display the results
        print(f"Time (UTC Offset): {current.get('time')}")
        print(f"Temperature: {current.get('temperature')} °C")
        print(f"Wind Speed: {current.get('windspeed')} km/h")
        print(f"Wind Direction: {current.get('winddirection')} degrees")
        
        # Open-Meteo uses a 'weathercode' that corresponds to a condition
        # You'd typically map this code to a description in a full application.
        print(f"Weather Code: {current.get('weathercode')} (See API docs for meaning)")
        
        print("\n--- Raw Data Snippet ---")
        # Print a snippet of the full response for inspection
        print(f"Timezone: {data.get('timezone')}")
        print(f"Units: {data.get('hourly_units')}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while making the API request: {e}")
        print("Please check your internet connection or the API endpoint URL.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
if __name__ == "__main__":
    # Ensure the 'requests' library is installed before running:
    # pip install requests
    
    # You can quickly change the location here for a one-off test:
    # PARAMS['latitude'] = 34.0522  # Los Angeles, CA
    # PARAMS['longitude'] = -118.2437
    # CITY_NAME = "Los Angeles, CA"
    
    # PARAMS['latitude'] = 0.3175  # Kamapla, Uganda
    # PARAMS['longitude'] = 32.5655
    # CITY_NAME = "Kamapala, Uganda"   

    PARAMS['latitude'] = 1.2921  # nairobi, Kenya
    PARAMS['longitude'] = 36.8219
    CITY_NAME = "Nairobi, Kenya"   
     
    get_current_weather(CITY_NAME, BASE_URL, PARAMS)