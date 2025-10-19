import random
from ascii_art import STAGES

WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    return random.choice(WORDS)

def display_game_state(mistakes, secret_word, guessed_letters):
    stage_index = min(mistakes, len(STAGES) - 1)
    print("=" * 40)
    print(STAGES[stage_index])
    masked = [ch if ch in guessed_letters else "_" for ch in secret_word]
    print("Word:    " + " ".join(masked))
    print("Guessed: " + (", ".join(sorted(guessed_letters)) if guessed_letters else "(none)"))
    print(f"Mistakes: {mistakes}/{len(STAGES)-1}")
    print("-" * 40)

def play_single_game():
    secret_word = get_random_word()
    guessed_letters = set()
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("\nWelcome to Snowman Meltdown!\n")

    while True:
        display_game_state(mistakes, secret_word, guessed_letters)

        # Win/Lose checks
        if all(letter in guessed_letters for letter in secret_word):
            print(f"You saved the snowman! The word was: {secret_word}\n")
            return True  # won
        if mistakes >= max_mistakes:
            print(f"Oh no! The snowman melted. The word was: {secret_word}\n")
            return False  # lost

        guess = input("Guess a letter: ").lower().strip()

        # Input validation: single alphabetic character
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one letter (a-z).\n")
            continue
        if guess in guessed_letters:
            print("You already tried that letter.\n")
            continue

        # Apply guess
        guessed_letters.add(guess)
        if guess not in secret_word:
            mistakes += 1
            print(f"Wrong! '{guess}' is not in the word.\n")
        else:
            print(f"Good job! '{guess}' is in the word.\n")

def ask_replay():
    while True:
        choice = input("Play again? [y/n]: ").strip().lower()
        if choice in ("y", "yes"):
            return True
        if choice in ("n", "no"):
            return False
        print("Please answer with 'y' or 'n'.")

def play_game():
    while True:
        _ = play_single_game()
        if not ask_replay():
            print("Thanks for playing! Goodbye.\n")
            break

if __name__ == "__main__":
    play_game()
