import random
from ascii_art import STAGES


WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """
    Return a random secret word to be guessed.

    Chooses one element from the global WORDS list using random.choice.
    The returned string represents the secret word for the current game.
    """
    return random.choice(WORDS)


def display_game_state(mistakes, secret_word, guessed_letters):
    """
    Display the current state of the game to the player.

    Args:
        mistakes (int): Number of incorrect guesses made so far.
        secret_word (str): The word the player is trying to guess.
        guessed_letters (set[str]): Letters guessed so far.

    Prints:
        The ASCII art stage, masked word display, guessed letters list,
        and number of mistakes out of the maximum possible.
    """
    stage_index = min(mistakes, len(STAGES) - 1)
    print("=" * 40)
    print(STAGES[stage_index])
    masked = [ch if ch in guessed_letters else "_" for ch in secret_word]
    print("Word:    " + " ".join(masked))
    print(
        "Guessed: "
        + (", ".join(sorted(guessed_letters)) if guessed_letters else "(none)")
    )
    print(f"Mistakes: {mistakes}/{len(STAGES) - 1}")
    print("-" * 40)


def play_single_game():
    """
    Play one complete round of Snowman Meltdown.

    Handles word selection, guesses, input validation, and win/loss logic.
    Returns:
        bool: True if the player wins (saves the snowman), False otherwise.
    """
    secret_word = get_random_word()
    guessed_letters = set()
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("\nWelcome to Snowman Meltdown!\n")

    while True:
        display_game_state(mistakes, secret_word, guessed_letters)

        # Win/Lose checks
        if all(letter in guessed_letters for letter in secret_word):
            print(f"You saved the snowman! The word was: {secret_word}\n")
            return True
        if mistakes >= max_mistakes:
            print(f"Oh no! The snowman melted. The word was: {secret_word}\n")
            return False

        guess = input("Guess a letter: ").lower().strip()

        # Input validation
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
    """
    Ask the player whether they want to play another round.

    Returns:
        bool: True if the player chooses to replay, False if not.
    """
    while True:
        choice = input("Play again? [y/n]: ").strip().lower()
        if choice in ("y", "yes"):
            return True
        if choice in ("n", "no"):
            return False
        print("Please answer with 'y' or 'n'.")


def play_game():
    """
    Manage the overall game session containing multiple rounds.

    Continues launching new rounds until the player declines to replay.
    Prints a farewell message upon exit.
    """
    while True:
        _ = play_single_game()
        if not ask_replay():
            print("Thanks for playing! Goodbye.\n")
            break


if __name__ == "__main__":
    play_game()
