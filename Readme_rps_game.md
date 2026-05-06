# Rock Paper Scissors, Python GUI Game

A polished **Rock-Paper-Scissors desktop game** built with Python and Tkinter. It features animations, score tracking, and a personalized player experience.

---

## What Makes This Project Interesting?

This isn’t just a basic game. It demonstrates:

* Event-driven programming using Tkinter
* Managing game states like scores and game flow
* GUI transitions from the start screen to the game screen
* Simple animations with `.after()`
* User-friendly design for interactions

---

## Gameplay Flow

1. Enter your name.
2. Choose Rock, Paper, or Scissors.
3. The computer makes a random move.
4. The score updates instantly.
5. The first to **10 points wins the match**.
6. An animated result screen appears:

   * Win → Celebration animation
   * Lose → Cry animation
7. The game resets automatically.

---

## Core Logic

```text
Rock     > Scissors  
Scissors > Paper  
Paper    > Rock
```

---

## Tech Stack

| Technology    | Purpose                  |
| ------------- | ------------------------ |
| Python        | Main programming         |
| Tkinter       | GUI and event handling   |
| Random Module | Generating computer moves |

---

## Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/developer-devashish/codsoft
# 2. Go into the folder
cd codsoft

# 3. Run the game
python rps_game.py
```

---

## Structure

```text
.
├── rps_game.py   # Main game file
└── README.md
```

---

## Highlights

* Name-based personalization
* Smooth UI transitions
* Animated win/lose screens
* Real-time score tracking
* Beginner-friendly yet well-structured

---

## Possible Upgrades

* Add sound effects
* Replace emojis with GIF animations
* Introduce difficulty levels
* Store high scores
* Convert to a web version

---

## Author

**Devashish Ghosh**  

---
