#Birthday Reminder - ver       by      Dr.M-Dev

import messagebox
from numpy.ma.core import size
from pandas.core.window.doc import kwargs_scipy
from rdflib.plugins.sparql.parserutils import value

ver = "0.1.1.21"
#====================IMPORTS:
from tkinter import *
import customtkinter
from PIL import Image, ImageTk
from customtkinter import CTkLabel, CTkImage, CTkCanvas, CTkButton
#----time:
import datetime as dt
#----gif:
import ctk_gif_class
import single_run_gif
#SYSTEMs:
#----save:
import data_manager
#----sounds:
import audio_system
#----restart:
import sys
import os


#====================Font/Colors Constants:
BACKGROUND_COLOR = "LightYellow"
COMMON_FONT = ("Consolas", 14, "bold")

#====================SETUP
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
#-------------
root = customtkinter.CTk()
root.configure(fg_color=BACKGROUND_COLOR)
#
window_width = 660
window_height = 600
#
root.minsize(window_width,window_height)
root.maxsize(window_width,window_height)
root.config(padx=20,pady=20) #padding!
#-------------
root.title(f"Birthday Reminder {ver}")

#====================Logo / Icons:
#----bitmap
root.iconbitmap("images/cake_bitmap.ico") #<---------------ADD A BIT MAP & LOGO

# #----version on banner: #PLACED DOWN (near the main-loop) to place it on TOP!
# ver_num = customtkinter.CTkLabel(root ,text=f"{ver}", fg_color="transparent", bg_color="transparent", font=("Consolas", 14, "bold"))
# ver_num.place(x=5,y=180)


#====================Globals:
birthday_entry = {
    "name" : "",
    "b_day" : (0,0),
    "b_year" : 0
}
#old:
# b_day = (0,0) #stored as a tuple
# b_year = 0
#--------------------------
#-------------Widgets displacement
widgets_x_place = 20
widgets_y_place = 10
#|
buttons_x_displacement = 100
buttons_y_displacement = 100
#|
widgets_background = "pink"


##################APP BANNER GIF# :)
banner_gif = ctk_gif_class.CTkGIFLabel(root,gif_path="images/bday_reminder_banner.gif") #200x100 is ideal + #no need to start animation, it's part of its __init__ implementation
banner_gif.initiate_animation()
banner_gif.place(x=widgets_x_place-35,y=widgets_y_place+60)

#______________________________________________________________
print('''                                                                                                                                                  
                                                              ...::::.      ...::::::::    :.      .:.   
  5@@@@@@@@B!    &@@@@@@@&G:        ^G&@@@&P#@@@@B~          J@@@@@@@@@G.   #@@@@@@@@@@   .@@B    7@@?   
  G@@~::::J@@!   @@#     B@@.      :@@G::~&@@!::Y@@~         J@@~    ^@@B   #@@.           !@@J  .@@B    
  G@@     .@@Y   @@@    5&@#       ~@@!   B@&   :@@?         J@@:     &@#   #@@BBBBBBB      P@@: #@@.    
  7BP     .@@J   PBGGGGGB@@B       :BB^   B@&   :@@?         ~GP.     &@#   JGPYYYYYYY       &@# @@!     
  Y&&^....?@@7   #&P     J@@:  ##  ^&&~   B@&   ^@@?         ?@@7:  :7@@P   Y@& ......       ^@@@@P      
  P@@@@@@@@&?    &@B     ?@@:  ##  ~@@!   B@&   :@@?         ?@@@@@@@@#J    J&@@@@@@@@?       ?@@B  


                                                             !J!:                                                                
                                                              ^G@@&P7:                                                           
                                         .~7YGB#&&&&&&&#BG5?~:  .Y@@@@&G^                                                        
                                    :?P&@@@@@@@@@@@@@@@@@@@@@@@&G?J@@@@@&                                                        
                                .!G@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@P   ...                                                 
                              ~B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@BG&&@@@@                                              
                            ?&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&                                             
                          7@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&#GYP#&J                                            
                        .B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@!                                                
                       :&@@@@@@@@@@@@@@@@J7@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@P                                               
                      .@@@@@@@@@@@@@@@@#:  ^&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@G                                              
                      #@@@@@@@@@@@@@@&7      P@@@@@@@@@@@@@B&@@@@@@@&@@#&@@@@@@@@@@J                                             
                     !@@@@@@@@@@@@@&?         ^#@@@@&&@@@@@@#PPGB##? B@5#@#@@@@@@@@@:                                            
                     B@@@@@@@@@@@G~             ^B@@@&GG#@@@@@@@#~   .&#J@Y&@@@@@@@@G                                            
                     @@@@@@@@@@~                  .?#@@@&BGPGBBJ      .#5G&J@@@@@@@@@.                                           
                   .@@@@@@@@@7      !PB##B4^        .^JG#&&P:  ^4B###P4?!~!?@@@@@@@@^                                           
                   .@@@@@@@@#      !4~.. .~4^                 ~4~....~4^    #@@@@@@@^   .~                                      
               ~BJ :@@@@@@@@BJYYYYYYJJJJYJJJJJJJ?!.     .!?JYYYJJYYYJJJYYYYY&@@@@@@@P7: .G#?.                                   
            .?BG^  &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@?...5@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@?  .Y#5:                                 
          :5BJ.    @@@@@@@@@&PJJJJJJ????JJJJ5&@@@@@@@@@@@@@@@GYJJ??????JJJJJYB@@@@@@@@@Y     7BB~                               
        !GG~       .YGG@@@@B        ...       G@@@@@@@@@@@@@:     .::.        !@@@@&GP7        ^G#?                             
     .JB5:             &@@@Y      4P..P@G.    7@@@@@@@@@@@@&    ^:^B@@@P.      @@@@~             .J#5.                          
     J@J               &@@@5     G@@4Y&@@&    ?@@@@?::^#@@@&   ~@4^B@@@@#     .@@@@~              ^#&:                          
      .5#J.            &@@@5     ?@@@@@@@P    7@@@@.   ?@@@&   .@@@@@@@@Y     .@@@@~           .J#P:                            
        .?#P:          #@@@G      .JGBBY:     5@@@&    ^@@@@.    ?B&&#P^      :@@@@~         ^PBJ.                              
           ~BB!        7@@@@5.              :P@@@@J     #@@@&!.             .!&@@@&        7BG~                                 
             :5#J.      ?@@@@@@@@@@@@@@@@@@@@@@@@J      .#@@@@@@&&&&&&&@&&@@@@@@@B.     :5BY.                                   
               .J#!      .7G&&@@@@@@@@@@@@@@&&G7.         ^5#&@@@@@@@@@@@@@@@&BJ:       7!                                      


 ''')

print(f"**** WELCOME TO Birthday-Reminder {ver}   -by-    Dr.M-Dev ****")

#====================#====================#====================#==================#==================#==================
#_____________________________________________________RESTART SYSTEM______________________________________________________#
#RETRY:
def restart():
    """Restarts the current Python script."""
    python = sys.executable
    os.execl(python, python, *sys.argv)


#====================#====================#====================#==================#==================#==================
#====================#====================#====================#==================#==================#==================
#_____________________________________________________B-DAY CHECK & NOTIFICATION SYSTEM________________________________#
#ALL IN birthday_detector.py
# sort through data.json and check (day,month) if it matches a list of day/month from (0,0) to (30,12)



#====================#====================#====================#==================#==================#==================
#_____________________________________________________SAVE SYSTEM______________________________________________________#
#ALL IN data_manager.py



#====================#====================#====================#==================#==================#==================
#_________________________________________________________UIs__________________________________________________________#

#___________________________________________________________________________________\\INPUTS:
#_____________________________________________________________Name text-bar "entry":
name_entry_l = customtkinter.CTkLabel(root, text="Enter Name:", text_color="black", font=COMMON_FONT)
name_entry_l.place(x=widgets_x_place+2,y=widgets_y_place+370)
#
name_entry = customtkinter.CTkEntry(root, bg_color="transparent", fg_color=widgets_background, font=COMMON_FONT, text_color="black", width=250)
name_entry.place(x=widgets_x_place,y=widgets_y_place+400)


#_____________________________________________________________DATE INPUTS: (spin boxes)
x_shift = -180
#--------day drop-down menu:
day_drop_menu_LABEL = customtkinter.CTkLabel(root, text="Day", text_color="black", font=COMMON_FONT)
day_drop_menu_LABEL.place(x=widgets_x_place+197+x_shift,y=widgets_y_place+430)
#----
days_list = [str(day+1) for day in range(0,30)] #list configuration
#
day_drop_menu = customtkinter.CTkComboBox(root, values=days_list, state="readonly",text_color="black", width=60, fg_color=widgets_background, dropdown_fg_color="pink", dropdown_text_color="black", dropdown_hover_color="white", button_color="hotpink")
day_drop_menu.set("0")
day_drop_menu.place(x=widgets_x_place+180+x_shift,y=widgets_y_place+460)

# #--------month drop-down menu:
month_drop_menu_LABEL = customtkinter.CTkLabel(root, text="Month", text_color="black", font=COMMON_FONT)
month_drop_menu_LABEL.place(x=widgets_x_place+257+x_shift,y=widgets_y_place+430)
# #----
months_list = [str(month+1) for month in range(0,12)] #list configuration
#
month_drop_menu = customtkinter.CTkComboBox(root, values=months_list,text_color="black" , state="readonly", width=60, fg_color=widgets_background, dropdown_fg_color="pink", dropdown_text_color="black", dropdown_hover_color="white" , button_color="hotpink")
month_drop_menu.set("0")
month_drop_menu.place(x=widgets_x_place+250+x_shift,y=widgets_y_place+460)

# #--------year drop-down menu:
year_drop_menu_LABEL = customtkinter.CTkLabel(root, text="Year", text_color="black", font=COMMON_FONT)
year_drop_menu_LABEL.place(x=widgets_x_place+257+88+x_shift,y=widgets_y_place+430)
#
year_entry = customtkinter.CTkEntry(root, bg_color="transparent", fg_color=widgets_background, font=COMMON_FONT, text_color="black", width=112)
year_entry.place(x=widgets_x_place+257+60+x_shift,y=widgets_y_place+460)


#_____________________________________________________________BUTTONS:
#0000#------------------------------ SAVE BIRTHDAY BUTTON!
save_noti_widget = single_run_gif.SingleGIFLabel(root,gif_path="images/saved_note.gif",gif_width=150,gif_height=55) #200x100 is ideal + #no need to start animation, it's part of its __init__ implementation
#
save_noti_widget.place(x=widgets_x_place+1000,y=widgets_y_place+1000) #<---------CURRENTLY place it out of bounds "hide"
# save_noti_widget.show_gif() #<-----use this to show gif



#####-----------------------FUNCTION
# def remove_save_notification():
#     save_noti_widget.place(x=widgets_x_place + 1000, y=widgets_y_place + 1000)

def add_b_day():
    global birthday_entry
    #--#
    # REMINDER\\ data-slot structure:
    # birthday_entry = {
    #     "name" : "",
    #     "b_day" : (0,0),
    #     "b_year" : 0
    # }
    #
    birthday_entry["name"] = str(name_entry.get())
    birthday_entry["b_year"] = str(year_entry.get())
    #
    day_data = int(day_drop_menu.get())
    month_data = int(month_drop_menu.get())
    birthday_entry["b_day"] = (day_data,month_data)
    #------------------------------------
    if len(str(name_entry.get())) > 18:
        messagebox.showwarning(title="Long Name", message="A first name should not exceed 18 letters :)")
    else:
        data_manager.save_file(birthday_entry)
        #DEBUGS/CHECKS/WARNINGS were moved to data_manager.py
        #------------------------------------
        restart_check = data_manager.save_file(birthday_entry)
        if str(restart_check) == "404":
            restart()
        else:
            print(f"RECALL-RESTART-ERROR===============>{restart_check}")
        #------------------------------------
        save_noti_widget.show_gif()
        save_noti_widget.place(x=widgets_x_place+430,y=widgets_y_place+340)
        #
        audio_system.save_file_sound()


#####-----------------------THE BUTTON
save_bday_b_x_displace = 250
save_bday_b_y_displace = 230
#0000-Add b-day button
####-------------------------BUTTON-ART / IMAGES
b_day_save_b_norm_img = customtkinter.CTkImage(light_image=Image.open("images/cake_norm.png"),size=(150, 200))
b_day_save_b_hover_img = customtkinter.CTkImage(light_image=Image.open("images/cake_hover.png"),size=(150, 200))
b_day_save_b_clicked_img = customtkinter.CTkImage(light_image=Image.open("images/cake_clicked.png"),size=(150, 200))

####-------------------------BUTTON-CONSTRUCTION Widget
b_day_save_button = customtkinter.CTkButton(root, image=b_day_save_b_norm_img , text="", height=50, width=150,command=add_b_day, fg_color="transparent",border_width=0, hover=False)
b_day_save_button.place(x=buttons_x_displacement+save_bday_b_x_displace-70,y=buttons_y_displacement+save_bday_b_y_displace+37)

####-------------------------BUTTON-Aesthetic-functions
#----HOVER
def b_day_save_b_hover_in(event):
    b_day_save_button.configure(image=b_day_save_b_hover_img)
    audio_system.light_candle_sound()
def b_day_save_b_hover_out(event):
    b_day_save_button.configure(image=b_day_save_b_norm_img)
#bind events:
b_day_save_button.bind("<Enter>", b_day_save_b_hover_in)
b_day_save_button.bind("<Leave>", b_day_save_b_hover_out)

#----CLICK-STATE
def b_day_save_b_clicked(event):
    b_day_save_button.configure(image=b_day_save_b_clicked_img)
def b_day_save_b_unclicked(event):
    b_day_save_button.configure(image=b_day_save_b_norm_img)
#bind events:
b_day_save_button.bind("<ButtonPress-1>", b_day_save_b_clicked)
b_day_save_button.bind("<ButtonRelease-1>", b_day_save_b_unclicked)

####-------------------------Button Text Labels
save_b_day_button_l = customtkinter.CTkLabel(root, text=f"Save Birthday Date", font=COMMON_FONT, text_color="Black")
save_b_day_button_l.place(x=buttons_x_displacement+save_bday_b_x_displace-58,y=buttons_y_displacement+save_bday_b_y_displace+220)



#_____________________________________________________
#0000#------------------------------ START-OVER BUTTON!
#####-----------------------FUNCTION
def clear_entries():
    name_entry.delete(0, "end")
    #
    day_drop_menu.set("0")
    month_drop_menu.set("0")
    #
    year_entry.delete(0, "end")
    #
    audio_system.erase_input_sound()

#####-----------------------THE BUTTON
start_over_b_x_displace = -60
start_over_b_y_displace = 410
#0000-Add b-day button
####-------------------------BUTTON-ART / IMAGES
start_over_b_norm_img = customtkinter.CTkImage(light_image=Image.open("images/startover_norm.png"),size=(200, 50))
start_over_b_hover_img = customtkinter.CTkImage(light_image=Image.open("images/startover_hover.png"),size=(200, 50))
start_over_b_clicked_img = customtkinter.CTkImage(light_image=Image.open("images/startover_clicked.png"),size=(200, 50))

####-------------------------BUTTON-CONSTRUCTION Widget
start_over_button = customtkinter.CTkButton(root, image=start_over_b_norm_img , text="", height=50, width=150,command=clear_entries, fg_color="transparent",border_width=0, hover=False)
start_over_button.place(x=buttons_x_displacement+start_over_b_x_displace,y=buttons_y_displacement+start_over_b_y_displace)

####-------------------------BUTTON-Aesthetic-functions
#----HOVER
def start_over_b_hover_in(event):
    start_over_button.configure(image=start_over_b_hover_img)
def start_over_b_hover_out(event):
    start_over_button.configure(image=start_over_b_norm_img)
#bind events:
start_over_button.bind("<Enter>", start_over_b_hover_in)
start_over_button.bind("<Leave>", start_over_b_hover_out)

#----CLICK-STATE
def start_over_b_clicked(event):
    start_over_button.configure(image=start_over_b_clicked_img)
def start_over_b_unclicked(event):
    start_over_button.configure(image=start_over_b_norm_img)
#bind events:
start_over_button.bind("<ButtonPress-1>", start_over_b_clicked)
start_over_button.bind("<ButtonRelease-1>", start_over_b_unclicked)

####-------------------------Button Text Labels
#NO NEED it's written on it :)



#_____________________________________________________________Today's Date & Time:
#-GLOBAL VARs:
current_date_data = ""
start_tracking_time = False
#
online = False

#-WIDGET:
date_time_display = CTkLabel(root, text=current_date_data, fg_color="pink", corner_radius=15, text_color="black", font=("Consolas", 20, "bold"))
date_time_display.place(x=widgets_x_place+20,y=widgets_y_place-15)

#-FUNCTIONs:
def updating_date_data():
    ########################
    # print("DEBUG: TRACKING STARTED . . . . . .")#<<_DEBUG
    #
    calculate_date_data()
    #
    root.after(100, updating_date_data)


def calculate_date_data():
    global current_date_data
    global online
    ##############
    #-----------------------------------------------------------------UPDATE Date-Time
    now = dt.datetime.now()
    minute = now.minute
    hour = now.hour
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
    elif day_name == 6:
        day_of_the_week = "Sunday"
    else:
        day_of_the_week = "ERROR Day-Of-Week was not recognised"
        print(f"{day_of_the_week}\nWRITE TODAY AS NUMBER {now.weekday()}")
    #-----------------------
    #DEBUG
    if minute < 10:
        current_date_data = f"today's date is:  {hour}:0{minute} - {day_of_the_week} - /{day}/{month}/{year}"
    else:
        current_date_data = f"today's date is:  {hour}:{minute} - {day_of_the_week} - /{day}/{month}/{year}"
    # print(current_date_data) #<<_DEBUG
    #-----------------------
    date_time_display.configure(text=current_date_data)
    #
    if start_tracking_time:
        updating_date_data()
    ###################################################
    # startup sound after opening window:
    # -----------------------Start-Up sound:
    if not online:
        audio_system.startup_sound()
        online = True





#====================#====================#====================#==================#==================#==================
#__________________________________________________SECONDARY WINDOW____________________________________________________#
b_day_list_window_ON = False
####Imports:
import second_window_bits
# taking ->>>>  CheckDatesWindow()
####Globals:
current_page_n = 1 #by default
stored_data_slots = []
#
slots_count = 0
text_output_page1 = ""
text_output_page2 = ""
text_output_page3 = ""
text_output_page4 = ""

def check_dates_list():
    #____________________________________________________________________________________________________
    ##################Globals & Data
    global stored_data_slots
    #--
    global b_day_list_window_ON
    b_day_list_window_ON = True  # -->#IMPORTANT SWITCH (to disable click-able & hover images)\\
    # {-} #
    print("DEBUG: B-DAYS-LIST window activated")
    print(f"LANG PICK WINDOW STATE->>{b_day_list_window_ON}")
    b_day_list_button.configure(image=brows_days_b__disabled_image)
    b_day_list_button.configure(state="disabled")

    #____________________________________________________________________________________________________
    ##################SETUP: (establishing window)
    # ================
    # ================
    check_dates_window = second_window_bits.CheckDatesWindow(root)
    #just to keep the bitmap image online:
    icon_image = Image.open("images/saved_cake_bitmap.ico")
    icon_photo = ImageTk.PhotoImage(icon_image)
    # --
    check_dates_window.after(200, lambda: check_dates_window.wm_iconphoto(False, icon_photo))
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #DEV NOTE:
    #the title/bitmap were already established in second_window_bits.py in a CLASS
    #SO no need for these old settings:
    # check_dates_window = customtkinter.CTkToplevel(root)
    # check_dates_window.iconbitmap("images/saved_cake_bitmap.ico")
    # check_dates_window.title(f"Saved Birthday Dates :)")
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    # ================
    # ================minor tweaks:
    check_dates_window.attributes("-topmost", True) #--------> TO PLACE IT ON TOP
    #
    check_dates_window.configure(fg_color=BACKGROUND_COLOR)
    #
    check_dates_window.minsize(400, 600)
    check_dates_window.maxsize(400, 600)
    check_dates_window.config(padx=20, pady=20)
    # ================
    # ================old implementation: (keep if needed)
    # #NOW switching this window to TOP LEVEL so it can respond to commands
    # print("<!> WINDOW-2 is top level now <!>")
    # customtkinter.CTkToplevel(master=check_dates_window)


    # ____________________________________________________________________________________________________
    ##################Art / Images
    nb_canvas_width = 1000
    nb_canvas_height = 1541
    notebook_canvas = CTkCanvas(check_dates_window, width=nb_canvas_width, height=nb_canvas_height, background=BACKGROUND_COLOR)
    notebook_canvas.place(x=-20, y=-17)
    #----------------------------------BG:
    notebook_bg_img = PhotoImage(file="images/notebook_bg.png", width=600, height=800)
    #
    notebook_bg = notebook_canvas.create_image( 0,0,image =notebook_bg_img)
    notebook_canvas.moveto(notebook_bg, -5, -2)


    # ____________________________________________________________________________________________________
    ##################Text / Days-Tracker #->data_manager.py
    text_display = notebook_canvas.create_text(100, -2,
                                               text=f"",
                                               font=("Consolas", 15, "bold"),
                                               fill="black",
                                               justify="left",
                                               anchor="nw")
    #------------------------------
    # ==== # needed refresh:
    slots_count = 0
    text_output_page1 = ""
    text_output_page2 = ""
    text_output_page3 = ""
    text_output_page4 = ""
    # ===
    def update_data_slots_display():
        global current_page_n
        #
        global stored_data_slots
        stored_data_slots = data_manager.recall_saved_data()
        # ------------------------------------
        if stored_data_slots == "404":
            restart()
        else:
            print(f"RECALL-SAVE-ERROR===============>{stored_data_slots}")
        # ==== # needed refresh:
        global slots_count
        global text_output_page1
        global text_output_page2
        global text_output_page3
        global text_output_page4
        #4page limit because WHO has more than 120 birthdays to remember!?
        #PLUS 4 is my fav number :)
        #====
        # ----------------------------------Clean Pages for update:
        text_output_page1 = ""  # clear
        text_output_page2 = ""  # clear
        text_output_page3 = ""  # clear
        text_output_page4 = ""  # clear

        # ----------------------------------
        slots_grabbed = 0
        slots_count = 0
        #--
        for data_slots in stored_data_slots:
            if slots_grabbed < 30:
                text_output_page1 += f"\n{data_slots}"
                slots_grabbed +=1
            elif slots_grabbed < 60:
                text_output_page2 += f"\n{data_slots}"
                slots_grabbed +=1
            elif slots_grabbed < 90:
                text_output_page3 += f"\n{data_slots}"
                slots_grabbed +=1
            elif slots_grabbed < 120:
                text_output_page4 += f"\n{data_slots}"
                slots_grabbed +=1
            else:
                print("<!> DATA SLOTS OVERFLOW <!>")  # DEBUG
            # ----count slot:
            slots_count += 1
        print(f"SLOTS COUNT: SLOTS COUNT:{slots_count} & SLOTS GRABBED:{slots_grabbed} ")
        # ----------------------------------SHOWING 1st PAGE by default: "text_output_page1" [every page has 30 lines]
        #====
        current_page_n = 1 #reset page back to 1
        flip_page(current_page_n)

    # ____________________________________________________________________________________________________
    # ===================================Page Number Display:
    page_number_display = notebook_canvas.create_text(217, 712,
                                               text=f"",
                                               font=("Consolas", 12, "bold"),
                                               fill="red",
                                               justify="left",
                                               anchor="nw")
    #==================================Function & Sorting:
    def flip_page(page):
        global current_page_n
        #
        global text_output_page1
        global text_output_page2
        global text_output_page3
        global text_output_page4
        #-----------hard reset:
        notebook_canvas.itemconfig(text_display, text="") #clearing display
        #-----------
        if page == 1:
            notebook_canvas.itemconfig(text_display, text=f"{text_output_page1}")
            print(f"displaying PAGE{page}")
        elif page == 2:
            notebook_canvas.itemconfig( text_display,text=f"{text_output_page2}")
            print(f"displaying PAGE{page}")
        elif page == 3:
            notebook_canvas.itemconfig( text_display,text=f"{text_output_page3}")
            print(f"displaying PAGE{page}")
        elif page == 4:
            notebook_canvas.itemconfig( text_display,text=f"{text_output_page4}")
            print(f"displaying PAGE{page}")
        else:
            # when 4 < page > 0 then we restart to page 1 :)
            current_page_n = 1
            flip_page(1)
            print(f"displaying PAGE1")
        #---- updating page number display:
        notebook_canvas.itemconfig(page_number_display, text=f"Page:{current_page_n}/4")
    #|
    #|
    ########################### TO START DISPLAY
    update_data_slots_display()
    ###########################
    #|
    #|
    #===================================#Page Flip Buttons:
    # current_page_n -> is 1 #by default
    #--
    def flip_forward():
        global current_page_n
        current_page_n +=1
        flip_page(current_page_n)
        audio_system.flip_page_sound()
        #DEBUG:
        print("+FLIP-FORWARD")


    # _____________________________________________________BUTTONS\\
    # 0000#------------------------------ FLIP PAGE BUTTON!
    #####-----------------------FUNCTION
    #flip_forward() --> the function is placed above :)
    #####-----------------------THE BUTTON
    flip_page_b_x_displace = 4
    flip_page_b_y_displace = 30
    # 0000-Add b-day button
    ####-------------------------BUTTON-ART / IMAGES
    flip_forward_b_norm_img = customtkinter.CTkImage(light_image=Image.open("images/flip_page_norm.png"),
                                                      size=(40, 40))
    flip_forward_b_hover_img = customtkinter.CTkImage(light_image=Image.open("images/flip_page_hover.png"),
                                                       size=(40, 40))
    flip_forward_b_clicked_img = customtkinter.CTkImage(light_image=Image.open("images/flip_page_clicked.png"),
                                                     size=(40, 40))
    ####-------------------------BUTTON-CONSTRUCTION Widget
    flip_forward__button = customtkinter.CTkButton(check_dates_window, image=flip_forward_b_norm_img, text="",
                                                    height=40, width=40,
                                                    command=flip_forward, fg_color="#ffffff", border_width=1,
                                                    hover=False)
    flip_forward__button.place(x=flip_page_b_x_displace, y=flip_page_b_y_displace)
    ####-------------------------BUTTON-Aesthetic-functions
    # ----HOVER
    def flip_forward_b_hover_in(event):
        flip_forward__button.configure(image=flip_forward_b_hover_img)

    def flip_forward_b_hover_out(event):
        flip_forward__button.configure(image=flip_forward_b_norm_img)

    # bind events:
    flip_forward__button.bind("<Enter>", flip_forward_b_hover_in)
    flip_forward__button.bind("<Leave>", flip_forward_b_hover_out)

    # ----CLICK-STATE
    def flip_forward_b_clicked(event):
        flip_forward__button.configure(image=flip_forward_b_clicked_img)

    def flip_forward_b_unclicked(event):
        flip_forward__button.configure(image=flip_forward_b_norm_img)

    # bind events:
    flip_forward__button.bind("<ButtonPress-1>", flip_forward_b_clicked)
    flip_forward__button.bind("<ButtonRelease-1>", flip_forward_b_unclicked)
    #-----------------
    #TESTING PROTOTYPE SETUP:
    # flip_page_button = CTkButton(check_dates_window , text="Flip Page", command=flip_forward, font=("Consolas", 12, "bold"),
    #                              text_color="black", fg_color="pink", hover_color="#E75480",
    #                              width=25,
    #                              height=18,
    #                              corner_radius=20)
    # flip_page_button.place(x=150,y=562)



    # _____________________________________________________
    # 0000#------------------------------ CLEAR STORAGE BUTTON!
    #####-----------------------FUNCTIONs
    def select_date_to_remove():
        audio_system.delete_button_clicked_sound()
        #
        dialog = customtkinter.CTkInputDialog(
            text="<!>\nWrite the name of the person/entry\nto delete the date related to it:",
            title="Deleting A Birthday Date",
            fg_color=BACKGROUND_COLOR,
            entry_fg_color="#E75480",#->pink
            button_fg_color="#E75480",#->pink
            button_hover_color="#8B0000",#->dark-red
            entry_text_color="#000000",#->black
            button_text_color="#000000",#->black
            text_color="#000000",#->black
            font=COMMON_FONT
        )
        # _____________________________
        dialog.iconbitmap("images/saved_cake_bitmap.ico")
        # _____________________________Getting input:
        user_input = dialog.get_input()
        # _____________________________
        if user_input is not None:
            if user_input.strip() == "":
                messagebox.showinfo(title="No Name Entered", message="Please write a birthday date name to remove!")
            else:
                data_manager.delete_date(user_input)
        else:
            messagebox.showinfo(title="Deletion Canceled",
                                message="Nothing was deleted, retuning to note book browser :)")
        #_________________________________________
        #________________________________old setup:
        # data_slot_name = delete_dialog_window.open_input_dialog()
        # data_manager.delete_date(data_slot_name)
        ###
        ### ON CLOSING DIALOG WINDOW:
        #UPDATING NOTEBOOK TEXT DISPLAY ANYWAY!!!!! here:
        print("<!> closing dialog window + UPDATING NOTEBOOK DISPLAY <!>")
        update_data_slots_display()



    #####-----------------------THE BUTTON
    clean_storage_b_x_displace = 4
    clean_storage_b_y_displace = 80
    delete_b_dimension = 40
    # 0000-Add b-day button
    ####-------------------------BUTTON-ART / IMAGES
    clean_storage_b_norm_img = customtkinter.CTkImage(light_image=Image.open("images/delete_b_norm.png"),
                                                      size=(delete_b_dimension, delete_b_dimension))
    clean_storage_b_hover_img = customtkinter.CTkImage(light_image=Image.open("images/delete_b_hover.png"),
                                                    size=(delete_b_dimension, delete_b_dimension))
    flip_page_b_clicked_img = customtkinter.CTkImage(light_image=Image.open("images/delete_b_clicked.png"),
                                                      size=(delete_b_dimension, delete_b_dimension))

    ####-------------------------BUTTON-CONSTRUCTION Widget
    clean_storage__button = customtkinter.CTkButton(check_dates_window, image=clean_storage_b_norm_img, text="", height=delete_b_dimension, width=delete_b_dimension,
                                                command=select_date_to_remove, fg_color="#ffffff", border_width=1,
                                                hover=False)
    clean_storage__button.place(x=clean_storage_b_x_displace,y=clean_storage_b_y_displace)

    ####-------------------------BUTTON-Aesthetic-functions
    # ----HOVER
    def clean_storage_b_hover_in(event):
        clean_storage__button.configure(image=clean_storage_b_hover_img)

    def clean_storage_b_hover_out(event):
        clean_storage__button.configure(image=clean_storage_b_norm_img)

    # bind events:
    clean_storage__button.bind("<Enter>", clean_storage_b_hover_in)
    clean_storage__button.bind("<Leave>", clean_storage_b_hover_out)

    # ----CLICK-STATE
    def clean_storage_b_clicked(event):
        clean_storage__button.configure(image=flip_page_b_clicked_img)

    def clean_storage_b_unclicked(event):
        clean_storage__button.configure(image=clean_storage_b_norm_img)

    # bind events:
    clean_storage__button.bind("<ButtonPress-1>", clean_storage_b_clicked)
    clean_storage__button.bind("<ButtonRelease-1>", clean_storage_b_unclicked)


    #____________________________________________________________________________________________________
    ################## B-DAYS-LIST-WINDOW-OPTIONS END:
    def on_closing():
        #----
        global b_day_list_window_ON
        b_day_list_window_ON = False #-->#IMPORTANT SWITCH (to enable click-able & hover images)\\
        #
        b_day_list_button.configure(image=brows_days_b__norm_image)
        b_day_list_button.configure(state="normal")
        # {-} #
        print("DEBUG: B-DAYS window IS OFF")
        print(f"LANG PICK WINDOW STATE->>{b_day_list_window_ON}")
        #
        check_dates_window.destroy()  # Explicitly close the window


    check_dates_window.protocol("WM_DELETE_WINDOW", on_closing)
    ################END_mainloop:
    check_dates_window.mainloop()



#_________________________OPEN WINDOW-2 (Birthdays List) BUTTON____________________________\\
#0000-Switch-Lang Button
browse_bdays_x_displace = 250
browse_bdays_y_displace = 230

####-------------------------Button Text Labels
browse_bdays_list__l = customtkinter.CTkLabel(root, text=f"Birthdays List", font=COMMON_FONT, text_color="Black")
browse_bdays_list__l.place(x=buttons_x_displacement+browse_bdays_x_displace+136,y=buttons_y_displacement+browse_bdays_y_displace+220)

####-------------------------BUTTON-ART / IMAGES
bbdays_img_width = 200
bbdays_img_heigh = 140
brows_days_b__norm_image = customtkinter.CTkImage(light_image=Image.open("images/bday_list_norm.png"),size=(bbdays_img_width+20, bbdays_img_heigh))
brows_days_b__hover_in_image = customtkinter.CTkImage(light_image=Image.open("images/bday_list_hover.png"),size=(bbdays_img_width, bbdays_img_heigh))
brows_days_b__clicked_image = customtkinter.CTkImage(light_image=Image.open("images/bday_list_clicked.png"),size=(bbdays_img_width, bbdays_img_heigh))
brows_days_b__disabled_image = customtkinter.CTkImage(light_image=Image.open("images/bday_list_viewing.png"),size=(bbdays_img_width,bbdays_img_heigh))

####-------------------------BUTTON-MAIN-FUNCTIONS
# def switchL_button_event():
#----------------------------->THE MAIN FUNCTION OF THIS BUTTON ISS GETTING A NEW CARD ->  pick_language()

####-------------------------BUTTON-CONSTRUCTION Widget
b_day_list_button = customtkinter.CTkButton(root, image=brows_days_b__norm_image , text="", height=50, width=150,command=check_dates_list, fg_color="transparent",border_width=0, hover=False)
b_day_list_button.place(x=buttons_x_displacement+browse_bdays_x_displace+80,y=buttons_y_displacement+browse_bdays_y_displace+80)

####-------------------------BUTTON-Aesthetic-functions
#----HOVER
def switchL_b_hover_in(event):
    global b_day_list_window_ON
    if not b_day_list_window_ON:
        b_day_list_button.configure(image=brows_days_b__hover_in_image)
        audio_system.open_notebook_sound()
def switchL_b_hover_out(event):
    global b_day_list_window_ON
    if not b_day_list_window_ON:
        b_day_list_button.configure(image=brows_days_b__norm_image)
#bind events: ------------------------------------------------------------>AND BOUND TO "LP_Window_State" only allowed when it's FALSE "off"
b_day_list_button.bind("<Enter>", switchL_b_hover_in)
b_day_list_button.bind("<Leave>", switchL_b_hover_out)

#----CLICK-STATE
def switchL_b_clicked(event):
    global b_day_list_window_ON
    if not b_day_list_window_ON:
        b_day_list_button.configure(image=brows_days_b__clicked_image)
def switchL_b_unclicked(event):
    global b_day_list_window_ON
    if not b_day_list_window_ON:
        b_day_list_button.configure(image=brows_days_b__norm_image)
#bind events: ------------------------------------------------------------>AND BOUND TO "LP_Window_State" only allowed when it's FALSE "off"
b_day_list_button.bind("<ButtonPress-1>", switchL_b_clicked)
b_day_list_button.bind("<ButtonRelease-1>", switchL_b_unclicked)











#==============FIRST TRIGGER
#-----------------------Start tracking time:
updating_date_data()

#----version on banner:
ver_num = customtkinter.CTkLabel(root ,text=f"{ver}", fg_color="transparent", bg_color="transparent", font=("Consolas", 12, "bold"), text_color="black", height=8)
ver_num.place(x=70,y=343)

#==============END
root.mainloop()
