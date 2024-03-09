import customtkinter as ctk

class Frame(ctk.CTkFrame):
    def __init__(self, master:ctk.CTk, frame_width:int, frame_height:int):
        super().__init__(master, width = frame_width, height = frame_height)

        def show(self):
            self.grid(row = 0, column = 0, sticky = ctk.NSEW)

        def hide(self):
            self.grid_forget()