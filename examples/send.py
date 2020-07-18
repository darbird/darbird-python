import darbird

darbird.initialize('db_xxxx', 'xxxx')
voice = darbird.Voice
sms = darbird.SMS
mms = darbird.MMS
auth = darbird.Authy


response = auth.authverify('+234xxxxxx','xxxx')
print(response)

