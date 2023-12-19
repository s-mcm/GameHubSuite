#
# IMPORTS
# 
import tkinter as tk
from itertools import groupby


#
# CLASSES
#
class tictactoe(tk.Frame):

    board_size = 4

    # class constructor
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

#        self.title("Tic Tac Toe")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
#        self.minsize(300,300)

        # VARIABLES
        self.player = "X"
        self.moves = 0
        self.button_list = []

        # TITLE
        frm_title = tk.Frame(self)
        frm_title.grid(row=0, column=0) # packs the item onto the container so it is displayed
        self.lbl_title = tk.Label(
            master=frm_title,
            text=f"Player {self.player} to play",
            width=40, # measured in "text units"
            height=3,)
        self.lbl_title.grid(row=0, column=0)

        # GAME GRID
        frm_board = tk.Frame(self)
        frm_board.grid(row=1, column=0, padx=25, pady=25, sticky="nesw")
        for i in range(self.board_size):
            bntl = []
            for j in range(self.board_size):
                btn = tk.Button(
                    master=frm_board,
                    text = f" ",
                    padx=5,
                    pady=5,)
                btn.bind("<ButtonRelease-1>", self.on_click) # left click
                btn.bind("<Enter>", self.on_enter) # mouse enters box
                btn.bind("<Leave>", self.on_leave) # mouse exits box
                btn.grid(row=i, column=j, sticky="nesw")
                bntl.append(btn)
            frm_board.rowconfigure(i, weight=1)
            frm_board.columnconfigure(i, weight=1)
            self.button_list.append(bntl)

        # FOOTER
        frm_footer = tk.Frame(self)
        frm_footer.grid(row=2, column=0)
        btn_reset = tk.Button(
            master=frm_footer,
            text=f"Reset game",
            padx=5,
            pady=5,
            relief="flat",
            command = self.reset_board,)
        btn_reset.bind("<Enter>", self.on_enter)
        btn_reset.bind("<Leave>", self.on_leave)
        btn_reset.grid(row=0, column=0, padx=5, pady=5, sticky="nesw")

        btn_exit = tk.Button(
            master=frm_footer,
            text=f"Exit",
            padx=5,
            pady=5,
            relief="flat",
            command = self.destroy)
        btn_exit.bind("<Enter>", self.on_enter)
        btn_exit.bind("<Leave>", self.on_leave)
        btn_exit.grid(row=0, column=1, padx=5, pady=5, sticky="nesw")


    def on_click(self, e):
        # check if button is disabled via state (because the <Button-1> event is bound, it ignores state [for whatever reason])
        if e.widget['state'] == "disabled":
            return 
        
        # if text is blank, a move hasn't been played here yet
        if e.widget['text'] != " ":
            return
        
        # disable button since this space has now been played
        e.widget['state'] = "disabled"
        self.on_leave(e)
        e.widget['text'] = self.player
        self.moves += 1

        # check win
        if self.check_win():
            self.lbl_title['text'] = f"Player {self.player} wins!"
            self.freeze_board()
            return
        
        # if win isn't found and moves are equal to amount of spaces on the board, it must be a draw
        if self.moves >= (self.board_size * self.board_size):
            self.lbl_title['text'] = f"Tie!"
            self.freeze_board()
            return

        # change player
        if self.player == "X":
            self.player = "O"
        else:
            self.player = "X"

        self.lbl_title['text'] = f"Player {self.player} to play"


    def check_win(self):
        x = []
        # check columns
        for j in range(len(self.button_list)):
            for i in self.button_list:
                x.append(i[j]['text'])
            if self.all_equal(x):
                return True
            x.clear()

        # check rows
        for k in self.button_list:
            for l in k:
                x.append(l['text'])
            if self.all_equal(x):
                return True
            x.clear()
        return False
                

    def all_equal(self, iterable):
        if iterable[0] == " ":
            return False
        g = groupby(iterable)
        return next(g, True) and not next(g, False)


    def reset_board(self):
        global player, moves
        for i in range(self.board_size):
            for j in range(self.board_size):
                self.button_list[i][j]['text'] = " "
                self.button_list[i][j]['state'] = "normal"
        moves = 0
        player = "X"
        self.lbl_title['text'] = f"Player {player} to play"


    def freeze_board(self):
        for i in range(self.board_size):
            for j in range(self.board_size):
                self.button_list[i][j]['state'] = "disabled"


    def on_enter(self, e):
        if e.widget['state'] == "disabled": # disables highlighing when button is disabled
            return
        e.widget['background'] = "lightgrey"


    def on_leave(self, e):
        e.widget['background'] = 'SystemButtonFace'


#
# MAIN
#