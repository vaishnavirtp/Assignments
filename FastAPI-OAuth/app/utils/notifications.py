import smtplib
from smtplib import SMTPAuthenticationError, SMTPConnectError
from fastapi import HTTPException
from decouple import config


def send_email(receiver_email, email_body, email_subject):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(config("SENDER"), config("SENDER_APP_PASSWORD"))
        SUBJECT = email_subject
        TEXT = email_body
        message = "Subject: {}\n\n{}".format(SUBJECT, TEXT)
        server.sendmail(config("SENDER"), receiver_email, message)
        server.quit()
    except SMTPConnectError as e:
        raise HTTPException(status_code=502, detail="Error occured while connecting.")

    except SMTPAuthenticationError:
        raise HTTPException(
            status_code=403,
            detail="The username and/or password you entered is incorrect",
        )
