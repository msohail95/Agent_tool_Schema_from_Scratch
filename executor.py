import json

from tools.weather_tool import get_weather
from tools.search_tool import web_search
from tools.distance_tool import calculate_distance
from tools.email_tool import send_email
from validators import validate_arguments


def execute_tool(
    tool_name,
    arguments
):


    validate_arguments(
        tool_name,
        arguments
    )


    if tool_name == "get_weather":

        return get_weather(
            arguments["city"]
        )


    elif tool_name == "web_search":

        return web_search(
            arguments["query"]
        )


    elif tool_name == "calculate_distance":

        return calculate_distance(

            arguments["source"],

            arguments["destination"]

        )


    if tool_name == "get_weather":


        return get_weather(
            arguments["city"]
        )



    elif tool_name == "web_search":


        return web_search(
            arguments["query"]
        )



    elif tool_name == "calculate_distance":


        return calculate_distance(

            arguments["source"],

            arguments["destination"]

        )
    elif tool_name == "send_email":

        return send_email(

            arguments["receiver"],

            arguments["subject"],

            arguments["content"]

        )



    else:

        raise Exception(
            "Unknown tool"
        )