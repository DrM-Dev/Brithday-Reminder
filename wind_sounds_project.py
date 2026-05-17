#==============IMPORTS:
import winsound
import random
#----
import time




#-----------------------------------------------------------------Picking Quotes
with open("quotes.txt") as file:
    all_quotes = file.readlines()
    random_quote = random.choice(all_quotes)

#------------------
winsound.PlaySound(r"C:\Windows\Media\Windows Notify Calendar.wav",winsound.SND_FILENAME)
# |
time.sleep(10)
# |
# Stop all playing sounds
winsound.PlaySound(None, winsound.SND_PURGE)