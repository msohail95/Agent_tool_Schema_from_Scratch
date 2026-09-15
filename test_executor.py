from executor import execute_tool



result = execute_tool(

    "get_weather",

    {
        "city":"Khushab"
    }

)


print(result)