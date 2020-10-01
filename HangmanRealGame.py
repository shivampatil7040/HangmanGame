# This is a word game
import random

def print_scaffold(guesses, wd):
    if guesses == 1:
        print("Remaining Moves : 5")
        print("          ")
        print("          ")
        print(" 	 O   ")
        print(" 	\|/  ")
        print(" 	 |   ")
        print(" 	/ \  ")
        print("          ")
    elif guesses == 2:
        print("Remaining Moves : 4")
        print("          ")
        print("          ")
        print(" 	 O   ")
        print(" 	\|/  ")
        print(" 	 |   ")
        print(" 	/ \  ")
        print(" ---------")
    elif guesses == 3:
        print("Remaining Moves : 3")
        print("|         ")
        print("|         ")
        print("|	 O   ")
        print("|	\|/  ")
        print("|	 |   ")
        print("|	/ \  ")
        print("|---------")
    elif guesses == 4:
        print("Remaining Moves : 2")
        print("|_________")
        print("|         ")
        print("|	 O   ")
        print("|	\|/  ")
        print("|	 |   ")
        print("|	/ \  ")
        print("|---------")
    elif guesses == 5:
        print("Remaining Moves : 1")
        print("|_________")
        print("|    |    ")
        print("|         ")
        print("|	 O   ")
        print("|	\|/  ")
        print("|	 |   ")
        print("|	/ \  ")
        print("|---------")
    elif guesses == 6:
        print("Remaining Moves : 0")
        print("|_________")
        print("|    |    ")
        print("|    |    ")
        print("|	 O   ")
        print("|	\|/  ")
        print("|	 |   ")
        print("|	/ \  ")
        print("|---------")
        print("\nThe word was %s." % wd)
        print("\nYOU LOSE! TRY AGAIN!")
        print("\nWould you like to play again, type 1 for yes or 2 for no?")
        again = str(input("> "))
        again = again.lower()
        if again == "1":
            hangMan()
        return

def selectWord():
    file = open('Sample.csv')
    words = file.readlines()
    myword = 'a'
    while len(myword) < 4:  # makes sure word is at least 4 letters long
        myword = random.choice(words)
        myword = str(myword).strip('[]')
        myword = str(myword).strip("''")
        myword = str(myword).strip("\n")
        myword = str(myword).strip("\r")
    myword = myword.lower()
    return myword

def hangMan():
    guesses = 0
    word = selectWord()
    word_list = list(word)
    blanks = "_" * len(word)
    blanks_list = list(blanks)
    new_blanks_list = list(blanks)
    guess_list = []

    print("Let's play hangman!\n")
    print_scaffold(guesses, word)
    print("" + ' '.join(blanks_list))
    print("\n")
    print("Guess a letter.")

    while guesses < 6:
        guess = str(input("> "))
        guess = guess.lower()

        if len(guess) > 1:
            print("Stop cheating! Enter one letter at time.")
        elif guess == "":
            print("Don't you want to play? Enter one letter at a time.")
        elif guess in guess_list:
            print("You already guessed that letter! Here is what you've guessed:")
            print(' '.join(guess_list))
        else:
            guess_list.append(guess)
            i = 0
            while i < len(word):
                if guess == word[i]:
                    new_blanks_list[i] = word_list[i]
                i = i + 1

            if new_blanks_list == blanks_list:
                print("Your letter isn't here.")
                guesses = guesses + 1
                print_scaffold(guesses, word)

                if guesses < 6:
                    print("Guess again.")
                    print(' '.join(blanks_list))
            elif word_list != blanks_list:
                blanks_list = new_blanks_list[:]
                print(' '.join(blanks_list))

                if word_list == blanks_list:
                    print("\nYOU WIN! Here is your prize:")
                    print("\n")
                    print("Would you like to play again?")
                    print("Type 1 for yes or 2 for no.")
                    again = str(input("> "))
                    if again == "1":
                        hangMan()
                    quit()

                else:
                    print("Great guess! Guess another!")

hangMan()
