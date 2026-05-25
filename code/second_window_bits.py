#==========================IMPORTS
import customtkinter as ctk
from PIL import ImageTk, Image
#--------------------------
bitmap_img = Image.open("images/saved_cake_bitmap.ico")

class CheckDatesWindow(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title(f"Saved Birthday Dates :)")
        self.geometry("400x600")

        #bitmap_img:
        global bitmap_img
        bitmap_img = Image.open("images/saved_cake_bitmap.ico")
        self.my_icon = ImageTk.PhotoImage(bitmap_img)
        #
        self.wm_iconphoto(False, self.my_icon)

        # #------I WILL TRY:
        # check_dates_window.iconbitmap("images/saved_cake_bitmap.ico")
        # later

# Main Application Setup should look like:
#   sub_window = CheckDatesWindow(main_window_name)
