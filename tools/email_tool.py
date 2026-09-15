import smtplib
from email.message import EmailMessage



def send_email(
    receiver,
    subject,
    content
):


    sender = "@gmail.com"

    password = "yv"


    message = EmailMessage()


    message["From"] = sender

    message["To"] = receiver

    message["Subject"] = subject


    message.set_content(
        content
    )


    try:


        server = smtplib.SMTP(
            "smtp.gmail.com",
            587
        )


        server.starttls()


        server.login(
            sender,
            password
        )


        server.send_message(
            message
        )


        server.quit()


        return {

            "status":"success",

            "message":
            "Email sent"

        }


    except Exception as e:


        return {

            "status":"failed",

            "error":str(e)

        }