import customtkinter as ctk

class TicTacToe(ctk.CTk):
    def __init__(self, win_width:int, win_height:int):
        super().__init__()

        screen_width, screen_height = int(self.winfo_screenwidth() * 1.15), self.winfo_screenheight()
        win_xcoord, win_ycoord = ((screen_width - win_width) // 2), ((screen_height - win_height) // 2)

        self.title("Tic Tac Toe")
        self.geometry(f"{win_width}x{win_height}+{win_xcoord}+{win_ycoord}") # Aligning app window to the center of the screen

        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)

        self.mainloop()
