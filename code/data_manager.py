import json
from json import JSONDecodeError
from pathlib import Path
#
from tkinter import messagebox  #->> use message box on customtkinter!
#
import audio_system

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++SAVE SYSTEM
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
        ####
        #ACTIVATE RESTART:
        print("ACTIVATING RESTART BECAUSE FileNotFoundError in save_file()")
        restart_code = "404"
        return restart_code

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
        ####
        # ACTIVATE RESTART:
        print("ACTIVATING RESTART BECAUSE JSONDecodeError in save_file()")
        restart_code = "404"
        return restart_code
    #--------save check
    finally:
        print("[-----------------DATA PROCESSING COMPLETED [0] ----------------]")




#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++RECALL SYSTEM
def recall_saved_data():
    recalled_data_slots = [] #<-A list of all stored JSON birthday-dictionaries
    # _____________________________
    # DATA TEMPLATE:
    data_slot = {
        f"TEST": {
            #
            "Day": f"{0}",
            "Month": f"{0}",
            "Year": f"{0}",
        }
    }
    # _____________________________
    try:
        with open(r"data/data.json", "r") as data_file:
            recovered_data = json.load(data_file)
        # ----
        for data_slot in recovered_data.items():
            data_slot_piece = "" #<-Empty DATA-SLOT
            if data_slot[1]["Day"] == "0" or data_slot[1]["Month"] == "0" or data_slot[0] == "TEST": #<-----detect & skip any empty data-slot
                print("EMPTY DATA-SLOT SKIPPED")
            else:
                data_slot_piece = f"{data_slot[0]} b-day: {data_slot[1]["Day"]}/{data_slot[1]["Month"]}/{data_slot[1]["Year"]}"
                #----#
                recalled_data_slots.append(data_slot_piece)
        # ----
        print("[------------------------------------DATA SLOTS RECOVERED [+] -----------------------------------]")
        return recalled_data_slots
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
        print("[-----------------FILE NOT FOUND! NEW FILE WAS MADE, NO DATA SLOTS RECOVERED [-] ----------------]")
        ####
        # ACTIVATE RESTART:
        print("ACTIVATING RESTART BECAUSE JSONDecodeError in recall_saved_data()")
        restart_code = "404"
        return restart_code



#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxCEALR STORAGE
def delete_date(key_name):
    with open(r"data/data.json", "r") as data_file:
        data = json.load(data_file)  # --> TAKING stored data
        #--
        # key_name = messagebox.askquestion(title="Deleting A Birthday Date", message="Pick which birthday date to delete, by writing it's exact name").lower()
        #--
        try:
            #----------------
            if key_name != "":
                #Altering "deleting" a Data-slot\\ (making it empty)
                del data[f"{key_name}"]
                ####
                with open("data/data.json", "w") as file: # --> Assembling everything back together
                    json.dump(data, file, indent=4)
            #----------------NOTIFICATION:
            # messagebox.showinfo(title="Target Acquired", message=f"Birthday entry [{key_name}] have been deleted!")
        except KeyError:
            messagebox.showwarning(title="WRONG NAME", message="The date you wanted to delete had a typo, or doesn't exist! try again :(")
    #------------------------------------
    # DEBUG
    print(f"[-----------------DATA SLOT -{key_name}- WAS REMOVED [!] ----------------]")
    audio_system.deleting_data_slot_sound()



###################TESTING:
# birthday_entry = {
#     "name" : "TEST",
#     "b_day" : (2,2),
#     "b_year" : 2002
# }
# save_file(birthday_entry)
#__________________________
# print(f"{recall_saved_data()}\n{type(recall_saved_data())}")
