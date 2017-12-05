from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC85ef408937f20443a02efafdcc2a3190"
# Your Auth Token from twilio.com/console
auth_token  = "fdf1368f14f8f66461b652568b682791"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+19728155545",
    from_="+13104212377",
    body="Hello Sekhar!")

print(message.sid)