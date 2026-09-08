# 🎯 Number Guessing Game

A simple and interactive **Number Guessing Game built with Python** as part of my Syntecxhub internship.

The program randomly selects a secret number, and the player has to guess it. After every incorrect guess, the game provides a **higher/lower hint**. The number of attempts is tracked, and the player can choose different difficulty levels and replay the game.

## 🚀 Features

* 🎲 Randomly generates a secret number
* 🎚️ Multiple difficulty levels
* 💡 Provides higher/lower hints
* 🔢 Counts the number of attempts
* 🏆 Tracks the best/lowest number of attempts
* 🔄 Replay option
* ⚠️ Handles invalid user input
* 🖥️ Simple command-line interface

## 🛠️ Technologies Used

* **Python 3**
* `random` module
* Loops
* Conditional statements
* Functions
* Exception handling
* User input/output

## 🎮 Difficulty Levels

The game provides different number ranges depending on the selected difficulty.

| Difficulty | Number Range |
| ---------- | -----------: |
| Easy       |       1 – 50 |
| Medium     |      1 – 100 |
| Hard       |      1 – 500 |

## 📂 Project Structure

```text
Syntecxhub_Number_Guessing_Game/
│
├── number_guessing_game.py
└── README.md
```

## ▶️ How to Run

### 1. Install Python

Make sure Python 3 is installed on your computer.

Check your Python version:

```bash
python --version
```

or:

```bash
py --version
```

### 2. Clone the Repository

```bash
git clone https://github.com/nikhilzaware23-design/Syntecxhub_Number_Guessing_Game.git
```

### 3. Open the Project Folder

```bash
cd Syntecxhub_Number_Guessing_Game
```

### 4. Run the Game

```bash
python number_guessing_game.py
```

On Windows, you can also use:

```bash
py number_guessing_game.py
```

## 🧠 How the Game Works

1. The player selects a difficulty level.
2. The program generates a random number within the selected range.
3. The player enters a guess.
4. The program compares the guess with the secret number.
5. If the guess is too low, the game displays a **higher** hint.
6. If the guess is too high, the game displays a **lower** hint.
7. The number of attempts increases after each valid guess.
8. When the correct number is guessed, the score is displayed.
9. The game records the lowest number of attempts as the best score.
10. The player can choose to play again.

## 📚 Python Concepts Practiced

This project helped me practice important Python fundamentals:

* `random.randint()`
* `while` loops
* `if / elif / else`
* Functions
* Variables and data types
* User input
* Type conversion
* Exception handling
* Lists/dictionaries where required
* Program control flow

## 💻 Sample Gameplay

```text
================================
      NUMBER GUESSING GAME
================================

Select Difficulty:
1. Easy   (1-50)
2. Medium (1-100)
3. Hard   (1-500)

Enter your choice: 2

I have selected a number between 1 and 100.
Try to guess it!

Enter your guess: 35
Higher! Try again.

Enter your guess: 70
Lower! Try again.

Enter your guess: 52
Higher! Try again.

Enter your guess: 58

🎉 Congratulations!
You guessed the correct number!

Attempts: 4
Best Score: 4

Do you want to play again? (y/n): n

Thanks for playing!
```

## 🎯 Learning Outcome

Through this project, I gained practical experience in:

* Building a Python program from scratch
* Using loops and conditional logic
* Working with Python's `random` module
* Handling user input and invalid values
* Designing a simple interactive command-line application
* Using Git and GitHub for version control
* Organizing and documenting a software project

## 🔮 Future Improvements

Possible future enhancements include:

* Adding a graphical user interface using Tkinter
* Adding a countdown/timer
* Saving high scores permanently
* Adding player names
* Adding multiplayer functionality
* Creating a web-based version
* Adding sound effects and animations

## 👨‍💻 Author

**nikhil Zaware**

## 🏢 Internship

This project was developed as part of my **Syntecxhub Internship**.

**Repository:** `Syntecxhub_Number_Guessing_Game`

---

⭐ If you found this project useful, feel free to star the repository!
