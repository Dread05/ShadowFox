import random

WORDS = ['python', 'developer', 'hangman', 'interface', 'software', 'engineer', 'variable']

HANGMAN_STAGES = [
    '''
       -----
       |   |
           |
           |
           |
           |
    =========
    ''',
    '''
       -----
       |   |
       O   |
           |
           |
           |
    =========
    ''',
    '''
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    ''',
    '''
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    ''',
    '''
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    ''',
    '''
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    ''',
    '''
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    '''
]



def choose_word():
    return random.choice(WORDS)



def display_game_state(incorrect_guesses, correct_guesses, secret_word):
    print(HANGMAN_STAGES[len(incorrect_guesses)])
    word_display = [letter if letter in correct_guesses else '_' for letter in secret_word]
    print('Word: ' + ' '.join(word_display))
    print(f"Incorrect guesses: {', '.join(incorrect_guesses)}")
    print("\n")



def check_game_status(incorrect_guesses, correct_guesses, secret_word):
    if len(incorrect_guesses) >= len(HANGMAN_STAGES) - 1:
        print("You lost! The word was: " + secret_word)
        return True
    elif all(letter in correct_guesses for letter in secret_word):
        print("Congratulations! You've guessed the word: " + secret_word)
        return True
    return False



def get_valid_guess(guessed_letters):
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single alphabetic character ")
        elif guess in guessed_letters:
            print("You've already guessed that letter ")
        else:
            return guess



def play_hangman():
    secret_word = choose_word()
    correct_guesses = set()
    incorrect_guesses = set()
    guessed_letters = set()
    max_attempts = len(HANGMAN_STAGES) - 1
    while True:
        display_game_state(incorrect_guesses, correct_guesses, secret_word)
        guess = get_valid_guess(guessed_letters)

        guessed_letters.add(guess)

        if guess in secret_word:
            correct_guesses.add(guess)
            print(f"Good job! {guess} is in the word \n")
        else:
            incorrect_guesses.add(guess)
            print(f"Oops! {guess} is not in the word \n")
        if check_game_status(incorrect_guesses, correct_guesses, secret_word):
            break



def play_again():
    while True:
        response = input("Do you want to play again?(y/n): ").lower()
        if response == 'y':
            return True
        elif response == 'n':
            return False
        else:
            print("Please respond with 'y'or'n'")



def main():
    print("Welcome to Hangman")
    while True:
        play_hangman()
        if not play_again():
            print("Thanks for playing Goodbye")
            break

if __name__ == '__main__':
    main()
