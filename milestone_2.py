import random

word_list = ['Cherry', 'Plum', 'Strawberry', 'Kiwi', 'Apple'] #Creates a list of words
#print(word_list)

word_to_be_guessed = random.choice(word_list) #Choices a random word from word_list
#print(word_to_be_guessed)

guess = input("Please enter a single letter: ") #Asks the user to enter a letter and assigns it to the guess variable 
if len(guess) == 1 and guess.isalpha(): #Checks if guessed letter is a single character and an alphabetical letter
    print("Good guess!")

else:
    print("Oops! That is not a valid input")

