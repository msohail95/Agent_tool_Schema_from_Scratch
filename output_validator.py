def validate_weather_output(result):


    required = [

        "city",
        "temperature",
        "rain_probability"

    ]


    for field in required:

        if field not in result:

            raise Exception(
                f"Invalid weather response: {field}"
            )


    return result