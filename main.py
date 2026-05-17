import smtplib


#sender:
my_email = r"shysamsciencechannels@gmail.com"
my_email_pass = r"wfprafawhfqmmzyk" #<----------activate 2 steps authentication then App-Password to get this pass
#reciver:
yahoo_friend = r"drmpythontestingground@yahoo.com"

#=============================
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    #
    connection.login(user=my_email,password=my_email_pass)
    connection.sendmail(from_addr=my_email,to_addrs=yahoo_friend, msg="Subject: henlooo\n\nTHIS IS AN SMTP TEST!\n :P")

#=============================
# Transport Layer Security (TLS)
