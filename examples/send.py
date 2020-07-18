import darbird

darbird.initialize('db_ce73ac1ee14b66017996845649142c52a7769cdb2a1a4374ea8f87c400c542e3', '0981')
voice = darbird.Voice
sms = darbird.SMS
mms = darbird.MMS
auth = darbird.Authy


response = auth.authverify('+2348103141424','13958')
print(response)

