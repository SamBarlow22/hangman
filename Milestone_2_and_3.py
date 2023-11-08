import random

word_list = ['Cherry', 'Plum', 'Strawberry', 'Kiwi', 'Apple'] #Creates a list of words
#print(word_list)

word_to_be_guessed = random.choice(word_list) #Choices a random word from word_list
print(word_to_be_guessed)




def check_guess(guess):
    guess = guess.lower()
    if guess in word_to_be_guessed.lower():
        print(f"Good guess! {guess} is in the word")
    else:
        print(f"Sorry, {guess} is not in the word. Try again")




def ask_for_input():
    while True:
        guess = input("Guess a letter ")
        if len(guess) == 1 and guess.isalpha(): #Checks if guessed letter is a single character and an alphabetical letter
            break

        else:
            print("Invalid letter. Please enter a single alphabetical letter ")

    check_guess(guess)

ask_for_input()

