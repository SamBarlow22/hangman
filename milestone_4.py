import random

list_of_guesses = []

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_of_guesses = []

        self.word = random.choice(word_list) #Pick random word from word_list
        self.word_guessed = ['_' for _ in self.word] #Produces _ for each letter in word_guessed
        self.num_letters = len(set(self.word)) #Calculate number of unique letters in the word




        
def check_guess(guess, hangman_instance):
    guess = guess.lower()
    if guess in hangman_instance.word:
        print(f"Good guess! {guess} is in the word.")

        for i in range(len(hangman_instance.word)):
            if hangman_instance.word[i] == guess:
                hangman_instance.word_guessed[i] = guess
    
        hangman_instance.num_letters -= 1

    else:
        hangman_instance.num_lives -=1
        print(f"Sorry, {guess} is not in the word")
        print(f"You have {num_lives} lives left")



def ask_for_input(hangman_instance):
    while True:
        guess = input("Guess a letter: ")
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid letter. Please enter a single alphabetical character. ")
        elif guess in hangman_instance.list_of_guesses:
            print("You already tried that letter!")
        else:
            check_guess(guess, hangman_instance)
            hangman_instance.list_of_guesses.append(guess)
            break


hangman_game = Hangman(word_list) #Creates an instance of the Hangman class


# Example usage:
print(hangman_game.word_guessed)
ask_for_input(hangman_game)




