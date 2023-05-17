# Hangman Game
# Created by Shounak Mukherjee

# Description

The Hangman Game is a text-based game where players attempt to guess a hidden word by guessing individual letters. This program allows players to enjoy the classic game on their computer.

# How It Works

At the start of the game, a word is randomly selected from a list of words stored in a file called "words.txt".
The chosen word is represented by a series of blank spaces, indicating the number of letters in the word.
The player enters a letter as a guess.
If the guessed letter is present in the chosen word, all instances of that letter are revealed in their respective positions. If the letter is not in the word, the player loses a try.
The game continues until the player guesses the entire word correctly or runs out of tries.
After each guess, the program displays the player's progress, the number of remaining tries, and the letters that have been guessed.
If the player guesses the word correctly, a congratulations message is displayed. If the player runs out of tries, the correct word is revealed.

# Implementation

The Hangman Game program is implemented using the Python programming language. Here's an overview of its structure and functionality:

The program utilizes object-oriented programming with a HangmanGame class to encapsulate the game logic and data.
The words are stored in a separate file named "words.txt". Each word is listed on a separate line in the file.
The program reads the words from the file and randomly selects one as the chosen word for the game.
The player's input is handled using the input() function in Python, allowing them to enter a letter for their guess.
The game validates the input, ensuring that the player enters a single letter and checks if it has already been guessed before.
The game keeps track of the guessed letters, the remaining tries, and updates the display accordingly after each guess.
The game continues until the player either guesses the word correctly or runs out of tries.
The program provides feedback to the player, informing them if their guess was correct or incorrect.
Once the game ends, a message is displayed to indicate whether the player won or lost, along with revealing the correct word.

# Key Concepts
Randomization: The program utilizes the random module in Python to select a random word from the list of words stored in the "words.txt" file. This adds variety to the game by choosing a different word each time.
File Handling: The program reads words from the "words.txt" file, which demonstrates the concept of file handling in Python. It opens the file, reads its contents, and extracts the words to be used in the game.
Object-Oriented Programming (OOP): The program employs the principles of OOP by using a HangmanGame class to encapsulate the game logic and data. This approach helps organize the code into reusable and modular components.
Data Structures: The program utilizes data structures to store and manipulate data efficiently. Specifically, it uses a list to store the words read from the file, and another list to keep track of the guessed letters.
Looping: The program employs loops, such as the while loop, to control the flow of the game. It continues running until a certain condition is met, such as the player correctly guessing the word or running out of tries.
Input Validation: The program validates user input to ensure it meets certain criteria. It checks if the input is a single letter and verifies if the letter has already been guessed. This helps maintain the integrity of the game and provides appropriate feedback to the player.
String Manipulation: The program manipulates strings to represent the hidden word and the player's progress. It replaces specific characters with blank spaces or reveals the correctly guessed letters in their respective positions.
Conditional Statements: The program utilizes conditional statements, such as if and else, to implement different behaviors based on certain conditions. It determines if a guessed letter is correct or incorrect, and adjusts the game state accordingly. 
