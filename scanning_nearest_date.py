#========================IMPORTS:
from datetime import date, datetime
#----
import json
#----
import messagebox
from pathlib import Path
#========================Globals:
nearest_birthday = [] #here we store entry-name, days-left,
                                    # then get it into a function "calculate_nearest_birthday"
                                    # to "return" it :)

def grab_data_slots():
    global nearest_birthday
    # _____________________________
    # DATA TEMPLATE:
    data_slot = {
        f"TEST": { #<-----------data_slot[0]
            #
            "Day": f"{0}",
            "Month": f"{0}",
            "Year": f"{0}",
        }
    }
    # _____________________________
    now = datetime.now()
    # _____________________________
    try:
        with open(r"data/data.json", "r") as data_file:
            recovered_data = json.load(data_file)
        # ----
        least_days_count = 400 #--->since a year is 356, so I just wanted to make it even xD "plus I love number 4" :)
        # ----
        for data_slot in recovered_data.items():
            if data_slot[1]["Day"] == "0" or data_slot[1]["Month"] == "0" or data_slot[0] == "TEST":  # <-----detect & skip any empty data-slot
                print("EMPTY DATA-SLOT SKIPPED")
            else:
                #now we calculate the date with the smallest amount of days left (making it the nearest birthday date) :)
                date_name=data_slot[0]
                month =int(data_slot[1]["Month"])
                day =int(data_slot[1]["Day"])
                year = now.year
                # ------------>   (Year, Month, Day)
                target_date = date(year, month, day)  # WE TAKE IT FROM THE data_manager.py (the nearest birthday date!) :D
                # &
                today = date.today()
                # ------------------------------------------ calculating days left
                days_left_count = (target_date - today).days
                # ------------ CHECKING IF THIS DATE IS CLOSER
                if days_left_count < least_days_count:
                    nearest_birthday.clear()
                    nearest_birthday.append(date_name)
                    nearest_birthday.append(days_left_count)
        #
        print("NEAREST DAY CALCULATING COMPLETED!")
        print(f"{nearest_birthday}")
        # ----


    #----
    except FileNotFoundError:
        messagebox.showerror(title="DATA FOLDER MOVED!",
                             message="data folder have been moved/deleted\n restart the program to start over :)")
        ####
        Path("data").mkdir(exist_ok=True)
        ####
        # +++++++++++++++++++++++++++
        print("file created")
        with open(r"data/data.json", "w") as data_file:
            json.dump(data_slot, data_file, indent=4)
        ####
        print("[-----------------FILE NOT FOUND! NEW FILE WAS MADE, NO DATA SLOTS RECOVERED [-] ----------------]")
        ####
        # ACTIVATE RESTART:
        print("ACTIVATING RESTART BECAUSE FileNotFoundError in recall_saved_data()")
        restart_code = "404"
        return restart_code
    #----



#=======================================================================================================================
def calculate_nearest_birthday():
    #------------------>   (Year,    Month,     Day)
    grab_data_slots()
    global nearest_birthday
    #----------------
    date_data = (f"{nearest_birthday[0]}",f"{nearest_birthday[1]}")
    print(f"NEAST BIRTHDAY IS {nearest_birthday[0]} which is {nearest_birthday[1]}-DAYS LEFT")
    return date_data #---->SEND A TUPLE (name of the birthday entry, days left)

#___________________________________________________________TEST-Launch:
# calculate_nearest_birthday()
