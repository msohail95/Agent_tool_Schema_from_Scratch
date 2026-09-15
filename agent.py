import json

from config import client, MODEL

from schemas.tool_schema import tools

from executor import execute_tool

from retry import retry


def run_agent(user_request):


    messages = [

        {
            "role":"system",

            "content":
            """
            You are a travel planning agent.

            You have access to tools.

            Always use the provided tools when they are needed.

            Never write function calls manually.
            Only use the tool calling mechanism.
            """
        },


        {
            "role":"user",

            "content": user_request
        }

    ]



    while True:


        response = client.chat.completions.create(


            model=MODEL,


            messages=messages,


            tools=tools,


            tool_choice="auto",

            temperature=0

        )



        message = response.choices[0].message



        # If LLM wants a tool

        if message.tool_calls:


            tool_call = message.tool_calls[0]


            tool_name = tool_call.function.name


            arguments = json.loads(
                tool_call.function.arguments
            )



            print(
                "\nCalling tool:",
                tool_name
            )


            print(
                "Arguments:",
                arguments
            )

            if tool_name == "send_email":

                approval = input(
                    "Send this email? (yes/no): "
                )

                if approval.lower() != "yes":
                    return "Email cancelled by user"

            result = retry(
                lambda:
                execute_tool(
                    tool_name,
                    arguments
                )
            )



            print(
                "Tool Result:",
                result
            )



            messages.append(

                message

            )



            messages.append(

                {

                "role":"tool",

                "tool_call_id":
                tool_call.id,

                "content":
                json.dumps(result)

                }

            )



        else:


            return message.content