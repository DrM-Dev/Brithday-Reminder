#=====================imports
import customtkinter as ctkinter
from PIL import Image

empty_img = ctkinter.CTkImage(Image.open("images/remove_saved_note.png"))

class SingleGIFLabel(ctkinter.CTkLabel):
    def __init__(self, master, gif_path, gif_width, gif_height, **kwargs):
        # Extract frames using Pillow
        self._gif = Image.open(gif_path)
        self._frames = []
        for i in range(self._gif.n_frames):
            self._gif.seek(i)
            # Create CTkImage for each frame
            self._frames.append(ctkinter.CTkImage(self._gif.copy(), size=(gif_width , gif_height)))  # Size can be dynamic
        #----inherit:
        super().__init__(master,text="" , image=self._frames[0], **kwargs)
        self._frame_index = 0
        # self.show_gif()#<------------------disabling this will make it run only once

    #-----------------Animation_fun
    n = 0

    def animate_gif(self):
        global n
        n+=1
        #
        global empty_img
        # ----------
        if n < 50:
            # Cycle through frames
            self._frame_index = (self._frame_index + 1) % len(self._frames)
            self.configure(image=self._frames[self._frame_index])
            # Update based on GIF frame duration (e.g., 100ms)
            self.after(30, self.animate_gif)
        else:
            self.configure(image=empty_img)

    def show_gif(self):
        global n
        n = 0
        # ----------
        self.animate_gif()

