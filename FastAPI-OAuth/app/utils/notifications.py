import smtplib
from smtplib import SMTPAuthenticationError, SMTPConnectError
from fastapi import HTTPException
from decouple import config


def send_email(receiver_email, email_body, email_subject):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(config("SENDER"), config("SENDER_APP_PASSWORD"))
        message = "Subject: {}\n\n{}".format(email_subject, email_body)
        server.sendmail(config("SENDER"), receiver_email, message)
        server.quit()
    except SMTPConnectError as e:
        raise HTTPException(
            status_code=502,
            detail="Smpt Error: Error occured while connecting to mail.",
        )

    except SMTPAuthenticationError:
        raise HTTPException(
            status_code=403,
            detail="Smpt Error: The username and/or password you entered is incorrect",
        )
