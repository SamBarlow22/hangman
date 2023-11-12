import random

class Hangman:
    """
    A class representing the Hangman game.

    Attributes:
        word_list (list): A list of words from which the game selects word to guess.
        num_lives (int): The number of lives the player has.
        guesses (list): A list to keep track of guessed letters.
        selected_word (str): The randomly chosen word from the word_list which the player will guess.
        word_guessed (list): A list representing the progress of guessing the word.
        letters_remaining (int): The number of unique letters remaining to guess in the word.

    Methods:
        check_guess(guess):
            Check if the guessed letter is in the selected word and update the game state.

        ask_for_input():
            Prompt the player to guess a letter and handle the input.
    """
    
    def __init__(self, word_list, num_lives=5):
        """
        Initialize a new Hangman game.

        Args:
            word_list (list): A list of words from which the game selects a word to guess.
            num_lives (int, optional): The number of lives the player has, which is set to 5.
        """
        
        self.word_list = word_list
        self.num_lives = num_lives
        self.guesses = []
        self.selected_word = random.choice(self.word_list).lower()
        self.word_guessed = ['_' for _ in self.selected_word]
        self.letters_remaining = len(set(self.selected_word))

    def check_guess(self, guess):
        """
        Check the guessed letter and update the game.

        Args:
            guess (str): The letter guessed by the player.
        """
        guess = guess.lower()
        found = False
        for i, letter in enumerate(self.selected_word):
            if letter == guess:
                self.word_guessed[i] = guess
                found = True
        if found:
            print(f'Good guess! {guess} is in the word.')
            self.letters_remaining -= 1
        else:
            self.num_lives -= 1
            print(f'Sorry, {guess} is not in the word')
            print(f'You have {self.num_lives} lives left')

    def ask_for_input(self):
        """
        Ask the player to guess a letter and handle their input.
        """
        while True:
            guess = input("Guess a letter: ")
            if len(guess) != 1 or not guess.isalpha():
                print('Invalid letter. Please enter a single alphabetical character. ')
            elif guess in self.guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.guesses.append(guess)
                print('Updated word: ', self.word_guessed)
                break

def play_game(word_list):
    """
    Play a game of Hangman.

    Args:
        word_list (list): A list of words from which the game selects a word to guess.
    """
    num_lives = 5
    game = Hangman(word_list, num_lives)

    print('Initial word: ', " ".join(game.word_guessed))

    while True:
        if game.num_lives == 0:
            print(f'You lost! The word was: {game.selected_word}')
            break

        if game.letters_remaining > 0:
            game.ask_for_input()
        else:
            print('Congratulations. You won the game!')
            break

word_list = ['cherry', 'plum', 'strawberry', 'kiwi', 'apple']

play_game(word_list)    
