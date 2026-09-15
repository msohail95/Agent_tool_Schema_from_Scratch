def validate_arguments(
    tool_name,
    arguments
):


    if tool_name == "get_weather":


        if "city" not in arguments:
            raise Exception(
                "Missing city parameter"
            )


        if not isinstance(
            arguments["city"],
            str
        ):
            raise Exception(
                "City must be text"
            )



    elif tool_name == "web_search":


        if "query" not in arguments:
            raise Exception(
                "Missing search query"
            )


        if len(arguments["query"]) < 3:

            raise Exception(
                "Search query too short"
            )



    elif tool_name == "calculate_distance":


        required = [
            "source",
            "destination"
        ]


        for field in required:

            if field not in arguments:

                raise Exception(
                    f"Missing {field}"
                )

    elif tool_name == "send_email":

        required = [

            "receiver",
            "subject",
            "content"

        ]

        for field in required:

            if field not in arguments:
                raise Exception(
                    f"Missing {field}"
                )


    return True