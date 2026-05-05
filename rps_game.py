import tkinter as tk
import random

# ---------------- GLOBAL VARIABLES ----------------
user_score = 0
computer_score = 0
player_name = ""

choices = ["Rock", "Paper", "Scissors"]

# ---------------- CELEBRATION WINDOW ----------------
def show_celebration():
    win = tk.Toplevel(root)
    win.title("🎉 You Won!")
    win.geometry("300x300")
    win.config(bg="black")

    label = tk.Label(win, text="🎉", font=("Arial", 50), bg="black", fg="yellow")
    label.pack(expand=True)

    msg = tk.Label(win, text=f"{player_name} Wins!", font=("Arial", 16, "bold"),
                   bg="black", fg="white")
    msg.pack()

    def animate(size=50, grow=True):
        if grow:
            size += 5
            if size > 80:
                grow = False
        else:
            size -= 5
            if size < 50:
                grow = True

        label.config(font=("Arial", size))
        win.after(100, animate, size, grow)

    animate()

# ---------------- CRY WINDOW ----------------
def show_cry():
    lose = tk.Toplevel(root)
    lose.title("😢 You Lost!")
    lose.geometry("300x300")
    lose.config(bg="#1e1e2f")

    label = tk.Label(lose, text="😢", font=("Arial", 50), bg="#1e1e2f", fg="lightblue")
    label.place(x=130, y=80)

    msg = tk.Label(lose, text="Better luck next time!",
                   font=("Arial", 14, "bold"),
                   bg="#1e1e2f", fg="white")
    msg.pack(side="bottom", pady=20)

    def animate(pos=0, direction=1):
        pos += direction * 5
        if pos > 20 or pos < 0:
            direction *= -1

        label.place(x=130, y=80 + pos)
        lose.after(100, animate, pos, direction)

    animate()

# ---------------- RESET GAME ----------------
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0

    score_label.config(text=f"Score → {player_name}: 0 | Computer: 0")
    result_label.config(text="")
    user_label.config(text=f"{player_name}'s Choice: ")
    comp_label.config(text="Computer Choice: ")

# ---------------- CHECK WINNER ----------------
def check_winner():
    if user_score == 10:
        show_celebration()
        reset_game()
    elif computer_score == 10:
        show_cry()
        reset_game()

# ---------------- GAME LOGIC ----------------
def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        result = f"{player_name} Wins!"
        user_score += 1
    else:
        result = "Computer Wins!"
        computer_score += 1

    user_label.config(text=f"{player_name}'s Choice: {user_choice}")
    comp_label.config(text=f"Computer Choice: {computer_choice}")
    result_label.config(text=result)

    score_label.config(
        text=f"Score → {player_name}: {user_score} | Computer: {computer_score}"
    )

    check_winner()

# ---------------- START GAME ----------------
def start_game():
    global player_name
    player_name = name_entry.get().strip()

    if player_name == "":
        warning_label.config(text="⚠ Please enter your name!", fg="red")
        return

    start_frame.pack_forget()
    game_frame.pack()

    title_label.config(text=f"{player_name} vs Computer")
    score_label.config(text=f"Score → {player_name}: 0 | Computer: 0")
    user_label.config(text=f"{player_name}'s Choice: ")

# ---------------- GUI SETUP ----------------
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("420x460")
root.config(bg="#1e1e2f")

# -------- START SCREEN --------
start_frame = tk.Frame(root, bg="#1e1e2f")

tk.Label(start_frame, text="Enter Your Name",
         font=("Arial", 16, "bold"),
         bg="#1e1e2f", fg="white").pack(pady=20)

name_entry = tk.Entry(start_frame, font=("Arial", 14))
name_entry.pack(pady=10)

tk.Button(start_frame, text="Start Game",
          font=("Arial", 12),
          bg="#4CAF50", fg="white",
          command=start_game).pack(pady=10)

warning_label = tk.Label(start_frame, text="",
                         font=("Arial", 10),
                         bg="#1e1e2f")
warning_label.pack()

start_frame.pack()

# -------- GAME SCREEN --------
game_frame = tk.Frame(root, bg="#1e1e2f")

title_label = tk.Label(game_frame, text="",
                       font=("Arial", 18, "bold"),
                       bg="#1e1e2f", fg="white")
title_label.pack(pady=10)

tk.Label(game_frame, text="First to 10 points wins!",
         font=("Arial", 12),
         bg="#1e1e2f", fg="lightgray").pack(pady=5)

# Buttons
btn_frame = tk.Frame(game_frame, bg="#1e1e2f")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Rock", width=10, bg="#4CAF50", fg="white",
          command=lambda: play("Rock")).grid(row=0, column=0, padx=5)

tk.Button(btn_frame, text="Paper", width=10, bg="#2196F3", fg="white",
          command=lambda: play("Paper")).grid(row=0, column=1, padx=5)

tk.Button(btn_frame, text="Scissors", width=10, bg="#f44336", fg="white",
          command=lambda: play("Scissors")).grid(row=0, column=2, padx=5)

# Labels
user_label = tk.Label(game_frame, text="",
                      font=("Arial", 12),
                      bg="#1e1e2f", fg="white")
user_label.pack(pady=5)

comp_label = tk.Label(game_frame, text="Computer Choice: ",
                      font=("Arial", 12),
                      bg="#1e1e2f", fg="white")
comp_label.pack(pady=5)

result_label = tk.Label(game_frame, text="",
                        font=("Arial", 14, "bold"),
                        bg="#1e1e2f", fg="yellow")
result_label.pack(pady=10)

score_label = tk.Label(game_frame, text="",
                       font=("Arial", 12),
                       bg="#1e1e2f", fg="lightgreen")
score_label.pack(pady=10)

# Run App
root.mainloop()