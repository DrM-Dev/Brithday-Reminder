import json
from json import JSONDecodeError
from pathlib import Path
#
import messagebox #->> use message box on customtkinter!


#--------------------------------- SAVE SYSTEM
def save_file(birthday_entry):
    ############
    birthday_name = birthday_entry["name"]
    day = birthday_entry["b_day"][0]
    month = birthday_entry["b_day"][1]
    year = birthday_entry["b_year"]
    #----
    birthday_entry_data = (day,month)
    #----
    #debug:
    print(
    f'NOTIFICATION:\nBIRTHDAY DATA SLOT SAVED:\nname:{birthday_name} - day:{birthday_entry["b_day"][0]} - month:{birthday_entry["b_day"][1]} - year:{birthday_entry["b_year"]}')
    print(f'\n\nFULL DATA PRINT DEBUG:{birthday_entry}')

    #_____________________________
    #DATA TEMPLATE:
    data_slot = {
        f"{birthday_name}": {
            #
            "Day": f"{str(day)}",
            "Month": f"{str(month)}",
            "Year": f"{str(year)}",
        }
    }
    #_____________________________SAVE:
    try:
        with open(r"data/data.json", "r") as data_file:
            updated_data = json.load(data_file)           #--> TAKING stored data
            updated_data.update(data_slot)  #--> updating said data
            print("DATA GRABBED")
            #####
        with open(r"data/data.json", "w") as data_file:
            json.dump(updated_data, data_file, indent=4) #--> RE-INSERTING IT BACK to the file
            print("UPDATED")
        # DEBUG
        print("[-----------------DATA SLOT WAS SAVED [+] ----------------]")

    #----------------------NO FILE:
    except FileNotFoundError:
        messagebox.showerror(title="DATA FOLDER MOVED!",
                             message="data folder have been moved/deleted\n restart the program to start over :)")
        ####
        Path("data").mkdir(exist_ok=True)
        ####
        #+++++++++++++++++++++++++++
        print("file created")
        with open(r"data/data.json", "w") as data_file:
            json.dump(data_slot, data_file, indent=4)
        ####
        print("[-----------------FILE NOT FOUND! NEW FILE WAS MADE, DATA SLOT WAS NOT SAVED [-] ----------------]")

    #-----------------------JSON-CODE-ERROR (if data.json) was tampered with:
    except JSONDecodeError:
        messagebox.showerror(title="DATA FOLDER CHANGED!",
                             message="data.json was altered \n restart the program to start over :)")
        ####
        Path("data").mkdir(exist_ok=True)
        ####
        # +++++++++++++++++++++++++++
        print("file created")
        with open(r"data/data.json", "w") as data_file:
            json.dump(data_slot, data_file, indent=4)
        ####
        print("[-----------------FILE NOT FOUND! NEW FILE WAS MADE, DATA SLOT WAS NOT SAVED [-] ----------------]")

    #--------save check
    finally:
        print("[-----------------DATA PROCESSING COMPLETED [0] ----------------]")


###################TESTING:
birthday_entry = {
    "name" : "TEST2",
    "b_day" : (2,2),
    "b_year" : 2002
}

save_file(birthday_entry)




