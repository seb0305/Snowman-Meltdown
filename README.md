# Snowman Meltdown
**ASCII Hangman Game: Guess Words or Watch the Snowman Melt! (7-Stage Animation)**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)

## 🎯 Features

| Feature | Description |
|---------|-------------|
| **7-Stage ASCII Animation** | Snowman melts progressively with wrong guesses (full → puddle) |
| **Word Guessing Game** | Guess secret words like "python", "github", "snowman" |
| **Progress Tracking** | Shows masked word, guessed letters, mistakes (out of 7) |
| **Input Validation** | Single a-z letter only; duplicates ignored |
| **Multiple Rounds** | "Play again?" – Endless replay until quit |

## 🏗️ Tech Stack

**Core:** Pure Python 3 (random, sets for letters)  
**ASCII Art:** 7 stages in `ascii_art.py` (STAGES list) 
**Game Logic:** `snowman.py` (main loop with validation) 

## 🚀 Quick Start

```bash
# Clone & run (no deps!)
git clone https://github.com/seb0305/Snowman-Meltdown.git
cd Snowman-Meltdown

# Start game
python snowman.py
# Or: python -m snowman
```

## 🎮 How to Play
1. Start Round

    Game picks random word (e.g., "python").

2. Guess Letters

    Input: "p" → Word: "p _ _ _ _ _" | Guessed: p

3. Snowman Melts

    Wrong → Next stage (1/7 mistakes) + ASCII update.

4. Win/Lose

    Fully guessed → "You saved the snowman!" | 7 mistakes → "The snowman melted."

5. Replay

    "y" for new round.

## 🧠 Core Algorithm
- STAGES: List of 7 ASCII strings (0=full, 6=melted puddle) [file:44].

- display_game_state: stage_index = min(mistakes, len(STAGES)-1) → Print art + mask + stats.

- Loop: Until word complete (all(letter in guessed_letters)) or mistakes >= 7.

- WORDS: ["python", "git", "github", "snowman", "meltdown"].


## 📝 Development
```bash
# Test functions
python -c "from ascii_art import STAGES; print(STAGES)"

# Add words
WORDS += ["new_word"]

# Debug
python snowman.py  # Fully documented!
```
## 🙌 Contributing
- Fork & clone

- Extend WORDS or STAGES (8th stage?).

- Test full round → Submit PR

## 📄 License
MIT - Free for educational use!