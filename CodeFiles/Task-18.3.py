import requests

def get_coordinates(city):
    """Get latitude and longitude for a given city using geocoding API"""
    url = f"https://nominatim.openstreetmap.org/search?q={city}&format=json"
    
    headers = {
        "User-Agent": "weather-app (your_email@example.com)"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise ValueError("Error fetching location data")

    data = response.json()

    if data:
        return float(data[0]['lat']), float(data[0]['lon'])
    else:
        raise ValueError("City not found")


def get_weather(lat, lon):
    """Get current weather for given latitude and longitude using Open-Meteo API"""
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

    response = requests.get(url)

    if response.status_code != 200:
        raise ValueError("Error fetching weather data")

    data = response.json()

    if 'current_weather' in data:
        return data['current_weather']
    else:
        raise ValueError("Weather data not found")


# Main function
if __name__ == "__main__":
    city = input("Enter city name: ")

    try:
        lat, lon = get_coordinates(city)
        weather = get_weather(lat, lon)

        print(f"\nCurrent weather in {city}:")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Wind Speed: {weather['windspeed']} km/h")
        print(f"Weather Code: {weather['weathercode']}")

    except ValueError as e:
        print(e)


        