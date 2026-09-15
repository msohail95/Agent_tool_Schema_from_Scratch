import requests


def get_coordinates(city):

    url = "https://geocoding-api.open-meteo.com/v1/search"


    params = {

        "name": city,

        "count": 1,

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
            f"Location not found: {city}"
        )


    location = data["results"][0]


    return (

        location["longitude"],

        location["latitude"]

    )



def calculate_distance(
        source,
        destination
):


    source_lon, source_lat = get_coordinates(source)


    dest_lon, dest_lat = get_coordinates(destination)



    url = (

        f"https://router.project-osrm.org/"
        f"route/v1/driving/"
        f"{source_lon},{source_lat};"
        f"{dest_lon},{dest_lat}"

        "?overview=false"

    )


    response = requests.get(
        url,
        timeout=10
    )


    response.raise_for_status()


    data = response.json()


    route = data["routes"][0]


    return {

        "from": source,

        "to": destination,

        "distance_km":
        round(
            route["distance"]/1000,
            2
        ),

        "travel_time_hours":
        round(
            route["duration"]/3600,
            2
        )

    }