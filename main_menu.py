#
# IMPORTS
# 
import tkinter as tk
import tictactoe


class MyButton(tk.Button):

    def __init__(self, *args, **kwargs):
        tk.Button.__init__(self, *args, **kwargs)
        self.padx=5,
        self.pady=5,
        self["relief"] = "flat",

        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        e.widget['background'] = "lightgrey"

    def on_leave(self, e):
        e.widget['background'] = 'SystemButtonFace'


class pages(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Menu")

        frm = tk.Frame(self, height=400, width=600)
        frm.grid(row=0, column=0, sticky="nesw")

        frm.grid_rowconfigure(0, weight=1)
        frm.grid_columnconfigure(0, weight=1)

        # dictionary of all frames
        self.frames = {}
        for F in (MenuPage, tictactoe.tictactoe):
            frame = F(frm, self)

            # pages class acts as the root window
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        # display main menu first
        self.show_frame(MenuPage)

    def show_frame(self, c):
        frame = self.frames[c]
        # raises the current frame to the top
        frame.tkraise()


class MenuPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        lbl_title = tk.Label(
            self,
            text=f"Main Menu",
            width=40,
            height=3,)
        lbl_title.grid(row=0, column=0)

        btn_tictactoe = MyButton(
            self,
            text = f"Tic Tac Toe",
            )
        btn_tictactoe.bind("<ButtonRelease-1>", lambda x : controller.show_frame(tictactoe.tictactoe))
        btn_tictactoe.grid(row=1, column=0)

        btn_exit = MyButton(
            self,
            text=f"Exit",
            command = controller.destroy,)
        btn_exit.grid(row=2, column=0, padx=5, pady=5)






obj = pages()
obj.mainloop()