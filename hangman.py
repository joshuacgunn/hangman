from wonderwords import RandomWord
import os
import time
import platform

def clearconsole(): #Used to clear console, this exists because linux and windows clear the console with different commands
    if platform.system() == 'Linux' or platform.system() == 'Darwin':
        os.system('clear') 
    elif platform.system() == 'Windows':
        os.system('cls')

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
    print(word)
    word_mutable = word #This variable is so the word can be manipulated without losing it

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
    hints_given = ['Hints: '] #List to hold hints given, 
    incorrect = 0 #Used to count how many incorrect guesses the user has inputted
    hint_given = 0
    print(HANGMANPICS[incorrect]) 
    newlength = word_length #newlength variable is for manipulating the word_length variable without directly changing it, used later 
    for und in list(word_length):
        if und == '_':
            idx3 = list(newlength).index(und)
            unknown_letter = word[idx3]
            break
    hints = ['placeholder', unknown_letter] #List to hold hints
    
    while '_' in word_length: #Loop used for guessing, ends when the whole word is guessed
        if incorrect > 5:  #Check if the player has lost
            playagain=input(f"You lost! the word was {''.join(word)}. Would you like to play again? yes/no: ")
            if playagain == "yes":
                clearconsole()
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
        
        if guess == 'hint': #Checks if user has inputted hint, and prints a hint based on how many times they've asked for one
            clear_lines(1)
            if len(hints_given) == 1:
                print(f'There are {vowel_count} vowels in the word.')
                hints_given.append(f'There is {vowel_count} vowel(s) in the word.')
                continue
            if hint_given == 0:
                print(f'The next unguessed letter is: {hints[1]}')
                hint_given += 1
                continue
            time.sleep(1)
            
            
        if guess in guess_list: #Checks if the user has already guessed a letter
            print("You already guessed that!")
            time.sleep(1)
            clear_lines(2)
            continue
        
        if len(guess) > 1: #Checks if the user entered a word, and prints whether it's correct or not
            if guess == ''.join(word):
                print("That's the right word!")
                newgame2 = input("Would you like to play again? yes/no: ")
                if newgame2 == 'yes':
                    clearconsole()
                    hangman()
                else:
                    quit()
            else:
                print(f"{guess} isn't the right word, sorry.")
                time.sleep(1)
                incorrect += 1
                clearconsole()
                print(newlength)
                print(f"You've guessed the following letters: {','.join(guess_list)}")
                print(''.join(hints_given))
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
            clearconsole()
            print(newlength)
            print(f"You've guessed the following letters: {','.join(guess_list)}")
            print(''.join(hints_given))
            print(HANGMANPICS[incorrect])
            continue

        if guess in word:
            print(f'{guess} is in the word!')
            time.sleep(1)
            guess_list.append(guess)
        clearconsole()
        
        for i in word_mutable:
            idx2 += 1 #Used to index where the letter is in the word
            if guess in i:
                idx=word_mutable.index(guess) #Indexes where the guessed letter is 
                word_length[idx]=guess #Replaces the underscore where the letter is with the letter
                word_mutable.remove(i) #Removes the underscore where the guessed letter is 
                word_mutable.insert(idx2, ' ') #This is done so the word has the same length, which is needed for proper indexing 
                newlength=''.join(word_length) #Variable that changes word_length into a string
        
        if 'hint' in guess_list: #Removes the word hint from guess_list
            guess_list.remove('hint')
        
        for i in guess_list: #This loop make sure the same letter doesn't appear in guess_list 
            if guess_list.count(i) > 1: 
                guess_list.remove(i)
        
        for und in list(word_length): #This is for telling the next unguessed word, I have no idea why it has to be here and at the top of loop, it just does. ¯\_(:~)_/¯
            if und == '_':
                idx3 = list(newlength).index(und)
                unknown_letter = list(word)[idx3]
                break
        
        #hints = [1, unknown_letter] #List to hold hints
        
        print(newlength)
        print(f"You've guessed the following letters: {','.join(guess_list)}")
        print(''.join(hints_given))
        print(HANGMANPICS[incorrect])
        
        if '_' not in newlength: #Final check, used when the word is fully guessed
            print(f'Congratulations, you guessed the word! it was {''.join(word)}')
            newgame = input("Would you like to play again? yes/no: ")
            if newgame == 'yes':
                clearconsole()
                hangman()
            else:
                quit()

clearconsole()
hangman()