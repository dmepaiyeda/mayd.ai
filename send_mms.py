# -*- coding: utf-8 -*-
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'XXXXXXX'
auth_token = 'XXXXXXX'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='Sample Photo',
         from_='XXXXXXX',
         media_url=['https://c1.staticflickr.com/3/2899/14341091933_1e92e62d12_b.jpg'],
         to='XXXXXXX'
     )

print(message.sid)
