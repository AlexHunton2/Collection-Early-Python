from twilio.rest import Client

accountSID = 'ACce4cd43934d43d5c506dc4c73f3ed971'
authToken = "6b8f32204b1818d2f60c5376fb3a429d"

twilioCli = Client(accountSID, authToken)
myTwilioNumber = +12562429007
recieverPhone = +4808250522

message = twilioCli.messages.create(body="Keon me me like big boys", from_=myTwilioNumber, to=recieverPhone)

