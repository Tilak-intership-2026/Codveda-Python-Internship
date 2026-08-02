# project: number guessing game
# developer: Tilak Kumar
#project number:2 from level 1 beginner
#Features
#Random Number Generation: Uses Python's random module to generate a secret number.
#Attempt Limit: Users have a maximum of 10 attempts to guess correctly.
#Real-time Feedback: Guides the user with hints after every incorrect guess.
#Input Validation: Handles non-numeric inputs gracefully without crashing#
import random
def start_guessing_game():
    print("--- Codveda Level 1: Number Guessing Game ---")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    max_attempts = 10
    attempts = 0

    print(f"I have selected a number between 1 and 100. You have {max_attempts} attempts to guess it!")

    while attempts < max_attempts:
        try:
            guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts}: Enter your guess: "))
            attempts += 1

            if guess == secret_number:
                print(f" Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                return
            elif guess < secret_number:
                print(" Too Low! Try a higher number.")
            else:
                print("Too High! Try a lower number.")

        except ValueError:
            print(" Invalid input! Please enter a valid integer.")

    print(f"\n Game Over! The correct number was {secret_number}. Better luck next time!")


if __name__ == "__main__":
    start_guessing_game()