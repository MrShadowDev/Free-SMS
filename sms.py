##Suscribe to https://youtube.com/@mrshadowdev
from twilio.rest import Client

SID = 'CHANGE_HERE'
Auth_Token = 'CHANGE_HERE''

cl = Client(SID, Auth_Token)

cl.messages.create(body='CHANGE_THE_TEXT_TO_SEND', from_='THE_NUMBER_PROVIDED_IN_TWILIO, to= 'PHONE_NUMBER_OF_RECEIVER')
