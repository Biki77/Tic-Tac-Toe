import tkinter as tk
def check_winner():
    global winner
    for combo in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]:
        if buttons[combo[0]]['text'] == buttons[combo[1]]['text'] == buttons[combo[2]]['text'] != '':
            buttons[combo[0]].config(bg='gray')
            buttons[combo[1]].config(bg='gray')
            buttons[combo[2]].config(bg='gray')
            winner = True
            label.config(text=f"Player {buttons[combo[0]]['text']} wins!")
            disable_buttons()
            return
    
    if all(button['text'] != '' for button in buttons):
        disable_buttons()

def button_click(index):
    global current_player
    if buttons[index]['text'] == '' and not winner:
        buttons[index]['text'] = current_player
        if current_player == 'X':
            buttons[index].config(fg='blue')
        else:
            buttons[index].config(fg='red')
        check_winner()
        if not winner:
            toggle_player()

def toggle_player():
    global current_player
    current_player = 'X' if current_player == 'O' else 'O'
    label.config(text=f"Player {current_player}'s turn")

def disable_buttons():
    for button in buttons:
        button.config(state=tk.DISABLED)

def reset_game():
    global current_player, winner
    current_player = 'X'
    winner = False
    label.config(text=f"Player {current_player}'s turn")
    for button in buttons:
        button.config(text='', state=tk.NORMAL, bg='black')
root = tk.Tk()
root.title('Tic-Tac-Toe')
root.configure(bg='black')
buttons = [tk.Button(root, text='', font=('normal', 25), width=6, height=2, bg='black', command=lambda i=i: button_click(i)) for i in range(9)]
for i, button in enumerate(buttons):
    button.grid(row=i // 3, column=i % 3)
current_player = 'X'
winner = False
label = tk.Label(root, text=f"Player {current_player}'s turn", font=('normal', 16), bg='gray')
label.grid(row=3, column=0, columnspan=3)
restart_button = tk.Button(root, text='Restart', font=('normal', 16), bg='green', command=reset_game)
restart_button.grid(row=4, column=0, columnspan=3)
root.mainloop()