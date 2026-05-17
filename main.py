#Birthday Reminder - ver       by      Dr.M-Dev
ver = "0.1.1"
#====================IMPORTS:
from tkinter import *
import customtkinter
from PIL import ImageTk, Image
from customtkinter import CTkImage, CTkLabel
#
from tkinter import messagebox
#
import random
#----NEW:
import sys
import os


#====================Font/Colors Constants:
BACKGROUND_COLOR = "#FFC0CB"
COMMON_FONT = ("Arial", 10, "bold")

#====================SETUP
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
#-------------
root = customtkinter.CTk()
root.configure(fg_color=BACKGROUND_COLOR)
#
window_width = 1000
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

####FLAG GIF:
#
# import ctk_gif_class
#
# flag_gif = ctk_gif_class.CTkGIFLabel(root,gif_path="images/usa_flag_gif.gif") #200x100 is ideal + #no need to start animation, it's part of its __init__ implementation
# flag_gif.place(x=window_width/4+590,y=window_height/4+30)

#====================Globals:
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
#====================#====================#====================#==================
#====================#====================#====================#==================
def run_code():
    pass







#_____________________________________________________________Starting the code with:
run_code()


#==============END
root.mainloop()