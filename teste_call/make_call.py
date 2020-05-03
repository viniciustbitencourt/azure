#!/usr/bin/env python3.6
import os 
from twilio.rest import Client
from urllib.parse import urlencode

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]

client = Client(account_sid, auth_token)
url = "https://twimlets.com/message?"
message = "Ola, Meu querido amigo, por favor receba essa mensagem com carinho."

call = client.calls.create(
        to=os.environ["MY_PHONE_NUMBER"],
        from_="+17192577149",
        url=url + urlencode({'Message': message}))


print(call.sid)
