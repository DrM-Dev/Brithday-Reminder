#Birthday Reminder - ver       by      Dr.M-Dev
ver = "0.1.1"
#====================IMPORTS:
from tkinter import *
import customtkinter
from PIL import ImageTk, Image
from customtkinter import CTkImage, CTkLabel
#
from tkinter import messagebox
#----gif:
import ctk_gif_class
#----restart:
import sys
import os


#====================Font/Colors Constants:
BACKGROUND_COLOR = "#FFC0CB"
COMMON_FONT = ("Courier", 14, "bold")

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
# root.iconbitmap("images/StatesFlashGame_bitmap.ico") #<---------------ADD A BIT MAP & LOGO
#----logo:
# logo = customtkinter.CTkImage(light_image=Image.open("images/LOGO_T_Black.png"),size=(110,100))
# logo_label = customtkinter.CTkLabel(root ,text="", fg_color="transparent" ,image=logo, bg_color="transparent")
# logo_label.place(x=5,y=180)



#BIRTHDAY CAKE GIF# :3
# import ctk_gif_class
#
# XXXXXX_gif = ctk_gif_class.CTkGIFLabel(root,gif_path="images/XXXXXX.gif") #200x100 is ideal + #no need to start animation, it's part of its __init__ implementation
# XXXXXX_gif.place(x=window_width/4+590,y=window_height/4+30)

#====================Globals:
birthday_entry = {
    "name" : "",
    "b_day" : 0,
    "b_month" : 0,
    "b_year" : 0,
    "date_day" : 0
}
#--------------------------
birthday = [0,0,0] # day/month/year A LIST to be stored
b_day = 0
b_month = 0
b_year = 0
#--------------------------
#-------------Widgets displacement
widgets_x_place = 20
widgets_y_place = 20
#|
buttons_x_displacement = 50
buttons_y_displacement = 50



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
name_entry = customtkinter.CTkEntry(root, bg_color="transparent", fg_color="white", font=COMMON_FONT, text_color="Black", width=250)
name_entry.place(x=widgets_x_place,y=widgets_y_place+400)


#_____________________________________________________________DATE INPUTS: (spin boxes)
date_ls = customtkinter.CTkLabel(root, text="Enter Name:", text_color="black", font=COMMON_FONT)
date_ls.place(x=widgets_x_place+2,y=widgets_y_place+370)
#




#_____________________________________________________________BUTTONS:
############################FUNCTION
def add_b_day():
    pass

############################THE BUTTON
# #0000-Add b-day button
# ####-------------------------Button Text Labels
# correct_b__label = customtkinter.CTkLabel(root, text=f"Get Another Card", font=("Courier", 14, "bold"), text_color="Black")
# correct_b__label.place(x=150+210+buttons_x_displacement,y=400+buttons_y_displacement+100)
#
# ####-------------------------BUTTON-ART / IMAGES
# new_card_b__normal_state_image = customtkinter.CTkImage(light_image=Image.open("images/cards_norm.png"),size=(150, 100))
# new_card_b__hover_in_image = customtkinter.CTkImage(light_image=Image.open("images/cards_hover.png"),size=(150, 100))
# new_card_b__clicked_image = customtkinter.CTkImage(light_image=Image.open("images/cards_clicked.png"),size=(150, 100))
#
# ####-------------------------BUTTON-MAIN-FUNCTIONS
# # def new_card_button_event():
# #----------------------------->THE MAIN FUNCTION OF THIS BUTTON ISS GETTING A NEW CARD ->  picking_state()
#
# ####-------------------------BUTTON-CONSTRUCTION Widget
# new_card_mark_button = customtkinter.CTkButton(root, image=new_card_b__normal_state_image , text="", height=50, width=150,command=add_b_day, fg_color="transparent",border_width=0, hover=False)
# new_card_mark_button.place(x=150+210+buttons_x_displacement,y=400+buttons_y_displacement)
#
# ####-------------------------BUTTON-Aesthetic-functions
# #----HOVER
# def new_card_b_hover_in(event):
#     new_card_mark_button.configure(image=new_card_b__hover_in_image)
# def new_card_b_hover_out(event):
#     new_card_mark_button.configure(image=new_card_b__normal_state_image)
# #bind events:
# new_card_mark_button.bind("<Enter>", new_card_b_hover_in)
# new_card_mark_button.bind("<Leave>", new_card_b_hover_out)
#
# #----CLICK-STATE
# def new_card_b_clicked(event):
#     new_card_mark_button.configure(image=new_card_b__clicked_image)
# def new_card_b_unclicked(event):
#     new_card_mark_button.configure(image=new_card_b__normal_state_image)
# #bind events:
# new_card_mark_button.bind("<ButtonPress-1>", new_card_b_clicked)
# new_card_mark_button.bind("<ButtonRelease-1>", new_card_b_unclicked)



#==============END
root.mainloop()