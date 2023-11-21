#
# IMPORTS
# 
import tkinter as tk
from itertools import groupby


#
# FUNCTIONS
#
def on_click(e):
    global player, moves
    
    # check if button is disabled via state (because the <Button-1> event is bound, it ignores state [for whatever reason])
    if e.widget['state'] == "disabled":
        return 
    
    # if text is blank, a move hasn't been played here yet
    if e.widget['text'] != " ":
        return
    
    # disable button since this space has now been played
    e.widget['state'] = "disabled"
    on_leave(e)
    e.widget['text'] = player
    moves += 1

    # check win
    if check_win():
        lbl_title['text'] = f"Player {player} wins!"
        freeze_board()
        return
    
    # if win isn't found and moves are equal to amount of spaces on the board, it must be a draw
    if moves >= (board_size * board_size):
        lbl_title['text'] = f"Tie!"
        freeze_board()
        return

    # change player
    if player == "X":
        player = "O"
    else:
        player = "X"

    lbl_title['text'] = f"Player {player} to play"


def check_win():
    x = []
    # check columns
    for j in range(len(button_list)):
        for i in button_list:
            x.append(i[j]['text'])
        if all_equal(x):
            return True
        x.clear()

    # check rows
    for k in button_list:
        for l in k:
            x.append(l['text'])
        if all_equal(x):
            return True
        x.clear()
        
    return False
            

def all_equal(iterable):
    if iterable[0] == " ":
        return False
    g = groupby(iterable)
    return next(g, True) and not next(g, False)


def reset_board():
    global player, moves
    for i in range(board_size):
        for j in range(board_size):
            button_list[i][j]['text'] = " "
            button_list[i][j]['state'] = "normal"
    moves = 0
    player = "X"
    lbl_title['text'] = f"Player {player} to play"


def freeze_board():
    for i in range(board_size):
        for j in range(board_size):
            button_list[i][j]['state'] = "disabled"


def on_enter(e):
    if e.widget['state'] == "disabled": # disables highlighing when button is disabled
        return
    e.widget['background'] = "lightgrey"

def on_leave(e):
    e.widget['background'] = 'SystemButtonFace'


#
# MAIN
#
window = tk.Tk()

# declarations 
button_list = []
board_size = 8
player = "X"
moves = 0

# create correct size button_list 
button_list = [[0] * board_size] * board_size

# store label in it's own frame
frm_title = tk.Frame(master=window)
frm_title.grid(row=0, column=0) # packs the item onto the container so it is displayed
lbl_title = tk.Label(
    master=frm_title,
    text=f"Player {player} to play",
    width=40, # measured in "text units"
    height=3
)
lbl_title.grid(row=0, column=0)


# store buttons in it's own frame
frm_board = tk.Frame(master=window)
frm_board.grid(row=1, column=0, padx=25, pady=25, sticky="nesw")
for i in range(board_size):
    for j in range(board_size):
        btn = tk.Button(
            master=frm_board,
            text = f" ",
            padx=5,
            pady=5,
        )
        btn.bind("<ButtonRelease-1>", on_click) # left click
        btn.bind("<Enter>", on_enter) # mouse enters box
        btn.bind("<Leave>", on_leave) # mouse exits box
        btn.grid(row=i, column=j, sticky="nesw")
        button_list[i][j] = btn
    frm_board.rowconfigure(i, weight=1)
    frm_board.columnconfigure(i, weight=1)


# store reset and exit in it's own frame
frm_footer = tk.Frame(master=window)
frm_footer.grid(row=2, column=0)
btn_reset = tk.Button(
    master=frm_footer,
    text=f"Reset game",
    padx=5,
    pady=5,
    relief="flat",
    command = reset_board
)
btn_reset.bind("<Enter>", on_enter)
btn_reset.bind("<Leave>", on_leave)
btn_reset.grid(row=0, column=0, padx=5, pady=5, sticky="nesw")

btn_exit = tk.Button(
    master=frm_footer,
    text=f"Exit",
    padx=5,
    pady=5,
    relief="flat",
    highlightcolor="blue",
    command = window.destroy
)
btn_exit.bind("<Enter>", on_enter)
btn_exit.bind("<Leave>", on_leave)
btn_exit.grid(row=0, column=1, padx=5, pady=5, sticky="nesw")

window.columnconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.minsize(300,300) 




window.mainloop() # run the window