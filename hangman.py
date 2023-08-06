# Instructions
# The task is to implement a word guessing game on the model of "Hangman". The game starts with a hidden word in which
# hyphens are displayed in place of letters. The player guesses a letter, and if the letter is in the word, the word
# display is updated to reveal the letter in place. If the word does not contain the letter guessed,
# the player gets one "strike".
#
# NOTE: you do not need to implement the drawing of the hanged man, as in the children’s game.
#
# If the player gets five strikes before all letters are revealed, the player loses. If the player is able to guess all
# letters before getting five strikes, the player wins.
#
# Requirements
# Your program should do the following:
#
# Include a function that take a word and list of letters guessed and returns a string that displays the letters guessed
# only, with hyphens in place of letters not guessed. HINT: You can loop over the letters in a word and concatenate
# a new word from letters and hyphens depending on whether a given letter is present in a list of letters guessed.
#
# Display the letters guessed so far to the user.
#
# Be able to handle user input in either uppercase or lowercase.
#
# Allow the user to quit the game by typing "quit".

def display_word(word, guessed_letters):
    answer_display = ''

    for letter in word:
        if letter.lower() in guessed_letters:
            answer_display += letter
        else:
            answer_display += '-'
    return answer_display

def hangman_game(hidden_word):
    # make sure the word is in lower case
    hidden_word = hidden_word.lower()

    # list to hold letters
    guessed_letters = []

    # strikes counter
    strikes = 0

    while True:
        guess = input('Enter a letter: ').lower()

        if guess == 'quit':
            print("didn't know you were a quitter, bye!")
            break

        if guess in guessed_letters:
            print('you have already used this letter, try again!')
        elif guess in hidden_word:
            guessed_letters.append(guess)
            print('good guess! current word: ', display_word(hidden_word, guessed_letters))
        else:
            strikes += 1
            print(f'wrong, you have {strikes} strikes. be careful')

        if display_word(hidden_word, guessed_letters) == hidden_word:
            print('congrats! you won!')
            break

        if strikes == 5:
            print('you have reached 5 strikes! the word was ', hidden_word)
            break


hangman_game('inst')
