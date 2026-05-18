#Birthday Reminder - ver       by      Dr.M-Dev
import time
from pandas.core.window.doc import kwargs_scipy
from rdflib.plugins.sparql.parserutils import value

ver = "0.1.1"
#====================IMPORTS:
from tkinter import *
import customtkinter
from PIL import Image
from customtkinter import CTkLabel
#----time:
import datetime as dt
#----gif:
import ctk_gif_class
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
window_width = 600
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

#----logo:
# logo = customtkinter.CTkImage(light_image=Image.open("images/LOGO_T_Black.png"),size=(110,100))
# logo_label = customtkinter.CTkLabel(root ,text="", fg_color="transparent" ,image=logo, bg_color="transparent")
# logo_label.place(x=5,y=180)


#====================Globals:
birthday_entry = {
    "name" : "",
    "b_day" : 0,
    "b_month" : 0,
    "b_year" : 0
}
#--------------------------
birthday = [0,0,0] # day/month/year A LIST to be stored
b_day = 0
b_month = 0
b_year = 0
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
import ctk_gif_class

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
#====================#====================#====================#==================#==================#==================
#_____________________________________________________B-DAY CHECK & NOTIFICATION SYSTEM________________________________#




#====================#====================#====================#==================#==================#==================
#_____________________________________________________SAVE SYSTEM______________________________________________________#





#====================#====================#====================#==================#==================#==================
#_________________________________________________________UIs__________________________________________________________#
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
day_drop_menu = customtkinter.CTkComboBox(root, values=days_list, state="readonly", width=60, fg_color=widgets_background, button_color="hotpink")
day_drop_menu.set("0")
day_drop_menu.place(x=widgets_x_place+180+x_shift,y=widgets_y_place+460)

# #--------month drop-down menu:
month_drop_menu_LABEL = customtkinter.CTkLabel(root, text="Month", text_color="black", font=COMMON_FONT)
month_drop_menu_LABEL.place(x=widgets_x_place+257+x_shift,y=widgets_y_place+430)
# #----
months_list = [str(month+1) for month in range(0,12)] #list configuration
#
month_drop_menu = customtkinter.CTkComboBox(root, values=months_list, state="readonly", width=60, fg_color=widgets_background, button_color="hotpink")
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
# REMINDER\\
# birthday_entry = {
#     "name" : "",
#     "b_day" : 0,
#     "b_month" : 0,
#     "b_year" : 0
# }

#####-----------------------FUNCTION
def add_b_day():
    global birthday_entry
    #--#
    birthday_entry["name"] = str(name_entry.get())
    birthday_entry["b_day"] = str(day_drop_menu.get())
    birthday_entry["b_month"] = str(month_drop_menu.get())
    birthday_entry["b_year"] = str(year_entry.get())
    #
    print(f'NOTIFICATION:\nBIRTHDAY DATA SLOT SAVED:\nname:{birthday_entry["name"]} - day:{birthday_entry["b_day"]} - month:{birthday_entry["b_month"]} - year:{birthday_entry["b_year"]}')


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
b_day_save_button.place(x=buttons_x_displacement+save_bday_b_x_displace,y=buttons_y_displacement+save_bday_b_y_displace+37)

####-------------------------BUTTON-Aesthetic-functions
#----HOVER
def b_day_save_b_hover_in(event):
    b_day_save_button.configure(image=b_day_save_b_hover_img)
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
save_b_day_button_l = customtkinter.CTkLabel(root, text=f"Click Me To Save This Birthday", font=COMMON_FONT, text_color="Black")
save_b_day_button_l.place(x=buttons_x_displacement+save_bday_b_x_displace-35,y=buttons_y_displacement+save_bday_b_y_displace+220)







#0000#------------------------------ START-OVER BUTTON!
#####-----------------------FUNCTION
def clear_entries():
    name_entry.delete(0, "end")
    #
    day_drop_menu.set("0")
    month_drop_menu.set("0")
    #
    year_entry.delete(0, "end")

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
#-GLOBAL VAR:
current_date_data = ""
start_tracking_time = False

#-WIDGET:
date_time_display = CTkLabel(root, text=current_date_data, fg_color="pink", corner_radius=15, text_color="black", font=("Consolas", 20, "bold"))
date_time_display.place(x=widgets_x_place,y=widgets_y_place-10)

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
    else:
        day_of_the_week = "ERROR Day-Of-Week was not recognised"
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


#-----------------------Start tracking time:
updating_date_data()
#-----------------------Trigger time tracking loop to start:



#==============END
root.mainloop()
