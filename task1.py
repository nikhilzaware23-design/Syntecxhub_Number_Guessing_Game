import random

# Best score for each difficulty
best_scores = {
    "easy": None,
    "medium": None,
    "hard": None
}

while True:
    print("\n==============================")
    print("      NUMBER GUESSING GAME")
    print("==============================")

    # Difficulty selection
    print("\nChoose difficulty:")
    print("1. Easy   (1 - 50)")
    print("2. Medium (1 - 100)")
    print("3. Hard   (1 - 500)")

    while True:
        choice = input("\nEnter your choice (1/2/3): ")

        if choice == "1":
            difficulty = "easy"
            max_number = 50
            break
        elif choice == "2":
            difficulty = "medium"
            max_number = 100
            break
        elif choice == "3":
            difficulty = "hard"
            max_number = 500
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

    # Generate random number
    secret_number = random.randint(1, max_number)

    attempts = 0

    print(f"\nI have selected a number between 1 and {max_number}.")
    print("Try to guess it!")

    # Guessing loop
    while True:
        try:
            guess = int(input("Enter your guess: "))

            if guess < 1 or guess > max_number:
                print(f"Please enter a number between 1 and {max_number}.")
                continue

        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Higher! 📈")
        elif guess > secret_number:
            print("Lower! 📉")
        else:
            print("\n🎉 Congratulations!")
            print(f"You guessed the number {secret_number}.")
            print(f"Number of attempts: {attempts}")
            break

    # Best score
    if best_scores[difficulty] is None:
        best_scores[difficulty] = attempts
        print("🏆 This is your best score!")
    elif attempts < best_scores[difficulty]:
        best_scores[difficulty] = attempts
        print("🏆 New best score!")
    else:
        print(f"Best score: {best_scores[difficulty]} attempts")

    # Display all best scores
    print("\n---------- BEST SCORES ----------")
    for level, score in best_scores.items():
        if score is None:
            print(f"{level.capitalize()}: Not played yet")
        else:
            print(f"{level.capitalize()}: {score} attempts")

    # what to play again y/n
    replay = input("\nDo you want to play again? (yes/no): ").lower()

    if replay not in ["yes", "y"]:
        print("\nThanks for playing! 👋")
        break