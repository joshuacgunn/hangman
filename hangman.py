from wonderwords import RandomWord
import os
import time

os.system('clear') #I do this so the console looks cleaner. Not really necessary
def clear_lines(n):
    #Clears the last 'n' lines in the terminal
    for _ in range(n):
        print("\033[F\033[K", end="")  #

todo = "Make hints a list of different hints, and change the conditional to print them out accordingly. Figure out a way to keep the hints even after a correct guess(It clears the entire console at the moment)."

r = RandomWord()
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''] #List for holding hangman pictures

def hangman():
    word = r.word()
    if word == "hint": #Lazy way to make sure the word isn't hint, as that would interfere with code later on
        hangman()
    
    word_length = ""
    for i in list(word): #Appends an underscore into word_length for each character in the word
        word_length += "_"
        if " " in i:
            word_length = list(word_length)
            space_index = word_length.index(i)
            word_length[space_index] == " "
            ''.join(word_length)

    word=list(word)
    if '-' in word: 
        word.remove('-')
    print(word_length)

    word2 = word #This variable is so the word can be manipulated without losing it

    vowel_count = 0 #Used for hints

    for i in word: #Counts the number of vowels in the word
        if (
            i == 'a'
            or i == 'e'
            or i == 'i'
            or i == 'o'
            or i == 'u'
        ):
            vowel_count += 1

    guess_list = [] #Used to keep track of guesses the user has made
    hints = [] #List to hold hints
    hints_given = [] #List to hold hints given, 
    incorrect = 0 #Used to count how many incorrect guesses the user has inputted
    
    print(HANGMANPICS[incorrect]) 
    newlength = word_length #newlength variable is for manipulating the word_length variable without directly changing it, used later 
    hints = 0
    while '_' in word_length: #Loop used for guessing, ends when the whole word is guessed
        if incorrect > 5:  
            playagain=input(f"You lost! the word was {''.join(word)}. Would you like to play again? yes/no: ")
            if playagain == "yes":
                os.system('clear')
                hangman()
            else:
                quit()
        guess = input("Enter a letter or word you want to guess, or type hint for a hint: ")
        guess = guess.lower()
        if guess.isalpha() == False: #Check for numbers in the input
            print("Numbers aren't letters.")
            time.sleep(1)
            clear_lines(2)
            continue
        if guess == 'hint' and hints == 0: #Checks if the user input is "hint", as well as the amount of hints used
            clear_lines(1)
            print(f'There are {vowel_count} vowels in the word.')
            hints += 1
            continue
        elif guess == 'hint' and hints == 1: 
            clear_lines(1)
            print(f'The first letter in the word is {word[0]}')
            hints += 1
            continue
        if guess in guess_list: 
            print("You already guessed that!")
            time.sleep(1)
            clear_lines(2)
            continue
        if len(guess) > 1: #Checks if the user entered a word, and prints whether it's correct or not
            if guess == ''.join(word):
                print("That's the right word!")
                newgame2 = input("Would you like to play again? yes/no: ")
                if newgame2 == 'yes':
                    os.system('clear')
                    hangman()
                else:
                    quit()
            else:
                print(f"{guess} isn't the right word, sorry.")
                time.sleep(1)
                incorrect += 1
                os.system('clear')
                print(newlength)
                print(f"You've guessed the following letters: {','.join(guess_list)}")
                print(HANGMANPICS[incorrect])
                continue
        
        word_length = list(word_length) #This is done so indexing and replacing can be done properly

        word = list(word) #Changes word to a list so it can be manipulated and indexed

        idx2 = -1 #Used for indexing where the letter is in the word

        if guess not in word:
            print(f'{guess} is not in the word!')
            guess_list.append(guess)
            time.sleep(1)
            incorrect += 1
            clear_lines(2)
            os.system('clear')
            print(newlength)
            print(f"You've guessed the following letters: {','.join(guess_list)}")
            print(HANGMANPICS[incorrect])
            continue

        if guess in word:
            print(f'{guess} is in the word!')
            time.sleep(1)
            guess_list.append(guess)

        for i in word2:
            idx2 += 1 #Used to index where the letter is in the word
            if guess in i:
                idx=word2.index(guess) #Indexes where the guessed letter is 
                word_length[idx]=guess #Replaces the underscore where the letter is with the letter
                word2.remove(i) #Removes the underscore where the guessed letter is 
                word2.insert(idx2, ' ') #This is done so the word has the same length, which is needed for proper indexing 
                newlength=''.join(word_length) #Variable that changes word_length into a string
        if 'hint' in guess_list: #Removes the word hint from guess_list
            guess_list.remove('hint')
        for i in guess_list: #This loop make sure the same letter doesn't appear in guess_list 
            if guess_list.count(i) > 1: 
                guess_list.remove(i)
        os.system('clear')
        print(newlength)
        print(f"You've guessed the following letters: {','.join(guess_list)}")
        print(HANGMANPICS[incorrect])
        if '_' not in newlength: #Final check, used when the word is fully guessed
            print(f'Congratulations, you guessed the word! it was {''.join(word)}')
            newgame = input("Would you like to play again? yes/no: ")
            if newgame == 'yes':
                os.system('clear')
                hangman()
            else:
                quit()
hangman()