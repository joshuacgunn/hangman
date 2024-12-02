from wonderwords import RandomWord
import os
import time
import platform
import random

def clearconsole(): #Used to clear console, this exists because linux and windows clear the console with different commands
    if platform.system() == 'Linux' or platform.system() == 'Darwin':
        os.system('clear') 
    elif platform.system() == 'Windows':
        os.system('cls')

def clear_lines(n):
    #Clears the last 'n' lines in the terminal
    for _ in range(n):
        print("\033[F\033[K", end="")  #

game_tracker = "previousgames.txt"

r = RandomWord() #wonderwords variable

hangmanpics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========
''','''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''','''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''','''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''','''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''','''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''','''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
'''] 

def hangman():
    word = r.word() #Generates the word and assigns it to a variable
    if word == "hint": #Lazy way to make sure the word isn't hint, as that would interfere with code later on
        hangman()
    
    hidden_word = ""
    for i in list(word): #Appends an underscore into hidden_word for each character in the word
        hidden_word += "_"
        if " " in i:
            hidden_word = list(hidden_word)
            space_index = hidden_word.index(i)
            hidden_word[space_index] == " "
            ''.join(hidden_word)

    word=list(word)
   
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
    
    word_guess_list = [] #Keep track of words guessed
    
    incorrect_guesses = 0 #Used to count how many incorrect_guesses guesses the user has inputted
    
    number_of_hints = 0 #Used to count how many hints have been given
    
    hint_index = 1 #This is used to properly pop and replace the vowels_left variable, it's needed as just using a number wouldn't work (I've tried many times)

    print(hidden_word)
    print(hangmanpics[incorrect_guesses]) 
    
    revealed_letters = hidden_word #revealed_letters variable is for manipulating the hidden_word variable without directly changing it, used later 
    
    for und in list(hidden_word):
        if und == '_':
            idx3 = list(revealed_letters).index(und)
            unknown_letter = word[idx3]
            break
        else:
            continue
    
    #The next couple of variables are for checking if a hint has been given, they're needed so the hint's list can be constantly updated
    first_hint_check = 0
    second_hint_check = 0
    fourth_hint_check = 0
    
    hints_given = ['Hints: ', ] #List to hold hints given,
    
    vowels_guessed = 0 #This holds how many vowels the user has guessed, it's also used for the vowels_left variable
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o','p','q','r','s','t','u','v','w','x','y','z'] #Needed to give random_letter variables later on
    
    while '_' in hidden_word: #Loop used for guessing, ends when the whole word is guessed
        def alwaysprint(): #This is what prints after every iteration, it's in function form so it doesn't have to be on a lot of different lines
            print(revealed_letters)
            if len(guess_list) > 0:
                print(f"You've guessed the following letters: {','.join(guess_list)}")
            if len(word_guess_list) > 0:
                print(f"You've guessed the following words: {', '.join(word_guess_list)}")
            print(hangmanpics[incorrect_guesses])
        
        vowels_left = vowel_count - vowels_guessed #Keeps track of the number of ungessed vowels in the word
        
        if len(hints_given) > 1 and number_of_hints > 0 and first_hint_check == 0: #This is for constantly updating vowels_left variable in the hints_given list, and printing it out. It needs to be here to work properly
            hints_given.pop(hint_index)
            hints_given.insert(hint_index, f'There are {vowels_left} vowels left in the word. ')
        if vowels_left == 0:
            first_hint_check = 1
        if number_of_hints > 0:
                clear_lines(1)
                print(''.join(hints_given[0:]))
        
        if incorrect_guesses > 5:  #Check if the player has lost
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

        if second_hint_check == 1 and guess == unknown_letter: #This is here to check and update hints_given if the user has inputted the unknown_letter variable
            if f'The next unguessed letter is {unknown_letter}. ' in hints_given:
                hints_given.remove(f'The next unguessed letter is {unknown_letter}. ')
        if fourth_hint_check == 1 and guess == random_letter_in_word:
            if f'The letter {random_letter_in_word} is in the word. ' in hints_given:
                hints_given.remove(f'The letter {random_letter_in_word} is in the word. ')

        random_letter_list = [] #List to hold the letter's the user has yet to guess, it's needed for random_letter variables

        for i in word: #This loop constantly updates random_letter_list so it only keeps letters that are unguessed
            if i not in guess_list and i != unknown_letter:
                random_letter_list.append(i)
        if len(random_letter_list) > 0:
            random_letter_in_word = random.choice(random_letter_list)

        if guess == 'hint': #Checks if user has inputted hint, and prints a hint based on how many times they've asked for one
            clear_lines(1)
            if vowels_left == 0 and number_of_hints == 0:
                number_of_hints += 1
            if number_of_hints == 0 and vowels_left > 0: #This hint gives the user the number of variables left
                number_of_hints += 1
                print(f'There are {vowels_left} vowels left in the word. ')
                hints_given.append(f'There are {vowels_left} vowels left in the word.')
                clear_lines(1)
            elif number_of_hints == 1 and second_hint_check == 0: #This hint gives the user the next unguessed letter
                hints_given.append(f'The next unguessed letter is {unknown_letter}. ')
                second_hint_check = 1
                number_of_hints += 1
            elif number_of_hints == 2: #This hint gives the user a random letter that is NOT in the word
                letters_in_word = list(word)
                for i in letters_in_word:
                    if i in letters:
                        letters.remove(i)
                for i in guess_list:
                    if i in letters:
                        letters.remove(i)
                random_letter_not_in_word = random.choice(letters)
                hints_given.append(f'The letter {random_letter_not_in_word} is not in the word. ')
                number_of_hints += 1
            elif number_of_hints == 3: #This hint gives the user a random letter that IS in the word and ISN'T guessed
                fourth_hint_check = 1
                hints_given.append(f'The letter {random_letter_in_word} is in the word. ')
                number_of_hints += 1
            elif number_of_hints == number_of_hints:
                print("Theres no more hints to give!")
                time.sleep(1)
                clear_lines(1)
            continue
        
        if guess in guess_list: #Checks if the user has already guessed a letter
            print("You already guessed that!")
            time.sleep(1)
            clear_lines(2)
            continue

        if len(guess) > 1: #Checks if the user entered a word, and prints whether it's correct or not
            if guess == ''.join(word):
                word_guess_list.append(guess)
                print(f"That's the right word! You used {number_of_hints} hint(s).")
                newgame2 = input("Would you like to play again? yes/no: ")
                if newgame2 == 'yes':
                    save_to_file = input("Would you like to save this game to a file? yes/no: ")
                    if save_to_file == 'yes':
                        print("Game state saved to previousgames.txt")
                        time.sleep(1)
                        with open(game_tracker, 'a') as file:
                            file.write(f"The word was: {revealed_letters}\nYou guessed the following letters: {','.join(guess_list)}\nYou guessed the following words: {''.join(word_guess_list)}\nYou used {number_of_hints} hints. {hangmanpics[incorrect_guesses]}")
                    clearconsole()
                    hangman()
                else:
                    quit()
            else:
                print(f"{guess} isn't the right word, sorry.")
                word_guess_list.append(guess)
                time.sleep(1)
                incorrect_guesses += 1
                clearconsole()
                alwaysprint()
                continue
        
        hidden_word = list(hidden_word) #This is done so indexing and replacing can be done properly

        word = list(word) #Changes word to a list so it can be manipulated and indexed

        idx2 = -1 #Used for indexing where the letter is in the word

        if guess not in word: 
            print(f'{guess} is not in the word!')
            guess_list.append(guess)
            time.sleep(1)
            incorrect_guesses += 1
            clearconsole()
            alwaysprint()
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
                hidden_word[idx]=guess #Replaces the underscore where the letter is with the letter
                word_mutable.remove(i) #Removes the underscore where the guessed letter is 
                word_mutable.insert(idx2, '.') #This is done so the word has the same length, which is needed for proper indexing 
                revealed_letters=''.join(hidden_word) #Variable that changes hidden_word into a string
        
        if 'hint' in guess_list: #Removes the word hint from guess_list
            guess_list.remove('hint')
        
        for i in guess_list: #This loop make sure the same letter doesn't appear in guess_list 
            if guess_list.count(i) > 1: 
                guess_list.remove(i)
        
        for und in list(hidden_word): #This is for telling the next unguessed word. !!!!IT NEEDS TO BE HERE AND AT THE TOP OF THE LOOP FOR PROPER FUNCTIONALITY!!!!
            if und == '_':
                idx3 = list(revealed_letters).index(und)
                unknown_letter = list(word)[idx3]
                break
            else:
                continue
        alwaysprint()
        vowels = ['a', 'e', 'i', 'o', 'u']
        if guess in vowels: #This is for counting the vowels the user has guessed that are in the word
            vowels_guessed += (list(revealed_letters).count(guess))
            vowels.remove(guess)
        if '_' not in revealed_letters: #Final check, used when the word is fully guessed
            print(f'Congratulations, you guessed the word! it was "{''.join(word)}". You used {number_of_hints} hint(s).')
            newgame = input("Would you like to play again? yes/no: ")
            if newgame == 'yes':
                save_to_file = input("Would you like to save this game to a file? yes/no: ")
                if save_to_file == 'yes': #Conditional to save game state to file
                    print("Game state saved to previousgames.txt")
                    time.sleep(1)
                    with open(game_tracker, 'a') as file:
                        file.write(f"The word was: {revealed_letters}\nYou guessed the following letters: {','.join(guess_list)}\nYou used {number_of_hints} hints. {hangmanpics[incorrect_guesses]}")
                clearconsole()
                hangman()
            else:
                quit()

clearconsole()
hangman() #Runs the game