from twilio.rest import Client 
 
account_sid = '[Put here the Account SID]'
auth_token = '[Put here the Auth Token]'
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='[Sender mobile number]',
                              body='[Type your message here!]',
                              to='[destination mobile nuber]'
                          ) 
 
print(message.sid)
