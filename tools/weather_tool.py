import requests


def get_coordinates(city):

    url = "https://geocoding-api.open-meteo.com/v1/search"

    params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    }


    response = requests.get(
        url,
        params=params,
        timeout=5
    )


    response.raise_for_status()


    data = response.json()


    if "results" not in data:
        raise Exception(
            f"City not found: {city}"
        )


    location = data["results"][0]


    return {

        "latitude": location["latitude"],
        "longitude": location["longitude"],
        "name": location["name"],
        "country": location.get("country","")

    }



def get_weather(city):


    # Step 1:
    # Convert city name to coordinates

    location = get_coordinates(city)


    lat = location["latitude"]
    lon = location["longitude"]


    # Step 2:
    # Get weather

    url = "https://api.open-meteo.com/v1/forecast"


    params = {

        "latitude": lat,

        "longitude": lon,

        "daily":
        [
        "temperature_2m_max",
        "precipitation_probability_max"
        ],

        "forecast_days":3

    }


    response = requests.get(
        url,
        params=params,
        timeout=5
    )


    response.raise_for_status()


    data = response.json()


    return {

        "city":
        location["name"],

        "country":
        location["country"],

        "temperature":
        data["daily"]["temperature_2m_max"][0],

        "rain_probability":
        data["daily"]["precipitation_probability_max"][0]

    }