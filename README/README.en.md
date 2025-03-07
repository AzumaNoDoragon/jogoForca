# Hangman Game in Python

This is a Hangman game implemented in Python, where the player tries to guess words related to specific themes. The drawing of the gallows is updated with each incorrect guess, and additional hints are provided after a certain number of mistakes.

## How it works

1. **Word Selection:**
   - A word, its theme, and a hint are randomly selected from a text file (`palavras.txt`).

2. **Gameplay:**
   - The player tries to guess the word by typing letters.
   - For each correct letter, the letter is revealed in the word.
   - For each incorrect letter, a part of the gallows drawing is added.
   - After a certain number of errors, an additional hint is displayed.
   - The game continues until the player guesses the word or the gallows drawing is complete.

## Requirements

- Python 3.x

## How to run

1. Make sure Python is installed.
2. Clone this repository or download the files.
3. Ensure there is a `palavras.txt` file in the same directory as the script, containing words, themes, and hints in the format `word - theme - hint`.
4. Run the script:

   ```sh
   python jogoForca.py
