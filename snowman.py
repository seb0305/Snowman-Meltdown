import random
from ascii_art import STAGES

WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    """Selects a random word from the list."""
    return random.choice(WORDS)

def display_game_state(mistakes, secret_word, guessed_letters):
    # Clamp mistakes to valid range to avoid IndexError during testing
    stage_index = min(mistakes, len(STAGES) - 1)
    print(STAGES[stage_index])

    # Build the word display with underscores for unguessed letters
    display_word = []
    for letter in secret_word:
        display_word.append(letter if letter in guessed_letters else "_")
    print("Word:", " ".join(display_word))

    # Optional status lines
    print("Guessed:", " ".join(sorted(guessed_letters)) if guessed_letters else "(none)")
    print(f"Mistakes: {mistakes}/{len(STAGES)-1}\n")

def play_game():
    secret_word = get_random_word()
    guessed_letters = set()
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!\n")

    while True:
        display_game_state(mistakes, secret_word, guessed_letters)

        # Check win before asking (covers case where word has repeats)
        if all(letter in guessed_letters for letter in secret_word):
            print("You saved the snowman! The word was:", secret_word)
            break

        if mistakes >= max_mistakes:
            print("Oh no! The snowman melted. The word was:", secret_word)
            break

        guess = input("Guess a letter: ").lower().strip()

        # Basic input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue
        if guess in guessed_letters:
            print("Already guessed that letter.\n")
            continue

        # Apply guess
        if guess in secret_word:
            guessed_letters.add(guess)
            print(f"Correct! '{guess}' is in the word.\n")
        else:
            guessed_letters.add(guess)
            mistakes += 1
            print(f"Wrong! '{guess}' is not in the word.\n")

if __name__ == "__main__":
    play_game()
