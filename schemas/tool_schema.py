tools = [

    {
        "type": "function",

        "function": {

            "name": "get_weather",

            "description":
            "Get weather information for a city",

            "parameters": {

                "type": "object",

                "properties": {

                    "city": {

                        "type": "string",

                        "description":
                        "City name"

                    }

                },

                "required": [
                    "city"
                ]

            }

        }

    },

    {
        "type": "function",

        "function": {

            "name": "send_email",

            "description":
            "Send the final travel plan by email after user approval",

            "parameters": {

                "type": "object",

                "properties": {

                    "receiver": {

                        "type": "string",

                        "description":
                        "Email address of recipient"

                    },

                    "subject": {

                        "type": "string"

                    },

                    "content": {

                        "type": "string",

                        "description":
                        "Email body"

                    }

                },

                "required": [

                    "receiver",

                    "subject",

                    "content"

                ]

            }

        }
    },


    {
        "type": "function",

        "function": {

            "name": "web_search",

            "description":
            "Search the internet for current information",

            "parameters": {

                "type": "object",

                "properties": {

                    "query": {

                        "type": "string",

                        "description":
                        "Search query"

                    }

                },

                "required":[
                    "query"
                ]

            }

        }

    },


    {
        "type":"function",

        "function": {

            "name":"calculate_distance",

            "description":
            "Calculate distance and travel time between two cities",

            "parameters": {

                "type":"object",

                "properties": {

                    "source":{

                        "type":"string"

                    },

                    "destination":{

                        "type":"string"

                    }

                },

                "required":[

                    "source",
                    "destination"

                ]

            }

        }

    }

]