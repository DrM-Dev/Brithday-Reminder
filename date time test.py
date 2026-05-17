#====================imports:
#time
import datetime as dt
#quotes-database
import pandas
import random
#email
import smtplib


#-----------------------------------------------------------------Fetch Date-Time
now = dt.datetime.now()
day = now.day
month = now.month
year = now.year
day_of_the_week = ""
#
day_name = now.weekday()#0->Monday  1->Tuesday 2->Wednesday 3->Thursday 4->Friday 5->Saturday
if day_name == 0:
    day_of_the_week = "Monday"
elif day_name == 1:
    day_of_the_week = "Tuesday"
elif day_name == 2:
    day_of_the_week = "Wednesday"
elif day_name == 3:
    day_of_the_week = "Thursday"
elif day_name == 4:
    day_of_the_week = "Friday"
elif day_name == 5:
    day_of_the_week = "Saturday"
else:
    day_of_the_week = "ERROR Day-Of-Week was not recognised"
#-----------------------
print(f"today's date is:  {day_of_the_week}-{day}/{month}/{year}")


#-----------------------------------------------------------------Picking Quotes
with open("quotes.txt") as file:
    all_quotes = file.readlines()
    random_quote = random.choice(all_quotes)


#OLD:
# quotes_file = pandas.read_csv("quotes.txt")
# #----
# quotes_list = quotes_file.values.tolist()
# #----
# refined_quotes = []
# for quote in quotes_list:
#     refine0 = str(quote)
#     refine1 = refine0.replace("[","")
#     refine2 = refine1.replace("]","")
#     refined_quotes.append(refine2)
# #----
# print(refined_quotes)
# #========================
# random_quote = random.choice(refined_quotes)
# #
# print(f"\n{random_quote}")


#-----------------------------------------------------------------
input("\n\nconform sending the quote by pressing RETURN/ENTER!")
#-----------------------------------------------------------------

my_email = r"shysamsciencechannels@gmail.com"
app_pass = r"wfprafawhfqmmzyk"
#
target_email = r"drmpythontestingground@yahoo.com"

with smtplib.SMTP("smtp.gmail.com") as mail_connection:
    mail_connection.starttls()
    #
    mail_connection.login(user=my_email,password=app_pass)
    mail_connection.sendmail(from_addr=my_email, to_addrs=target_email, msg=f"Subject: Testing Quotes Bot\n\n {random_quote}\n:3")
