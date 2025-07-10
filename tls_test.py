import python_certifi_win32
import ssl
import smtplib

context = ssl.create_default_context()
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls(context=context)
    print("TLS handshake successful!")
