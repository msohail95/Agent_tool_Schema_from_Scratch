from tools.email_tool import send_email



result = send_email(

    "msohailabbas08@gmail.com",

    "Travel Plan",

    """
    Your Murree trip plan is ready.
    """

)


print(result)