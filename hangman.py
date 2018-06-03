import csv
from random import randint
from string import ascii_uppercase, ascii_letters


MAX_TRIES = 9
CATEGORY = 'town'
WORDS_TO_USE = {'H': 1000, 'M': 250, 'L': 100}


def display_letter(letter_status):
    return letter_status[0] if letter_status[1] else '_'


def display_word(word_status):
    return ' '.join([display_letter(c) for c in word_status])


def main():
    with open('towns.csv', 'r') as towns_file:
        words = [row[0] for row in csv.reader(towns_file)]
    difficulty = input('Difficulty (H. M. L)?')
    difficulty = ('L' if difficulty.upper() not in ['H', 'M', 'L']
                  else difficulty)
    quiz_word_unparsed = words[randint(0, WORDS_TO_USE[difficulty])]
    word = ''.join([c.upper() for c in quiz_word_unparsed
                    if c.upper() in ascii_letters])
    guesses = set()
    word_status = [[letter, False] for letter in word]
    print('HANGMAN\nGuess the %s letter %s: %s' % (len(word), CATEGORY,
                                                     display_word(word_status)))
    tries = 0
    while tries < 9:
        guess = input('Guess a letter or the %s: ' % CATEGORY).upper()
        if not all(g in ascii_uppercase for g in guess):
            input('That\'s not a valid letter, please try again')
            continue
        if len(guess) == 1:
            if guess in word:
                if guess in guesses:
                    input('You\'ve already tried that, please try again')
                    continue
                else:
                    print('Good one!')
                    for c in word_status:
                        if c[0] == guess:
                            c[1] = True
            else:
                print('Sorry, %s isn\'t there' % guess)
        else:
            if guess == word:
                print('CONGRATULATIONS!!! You guessed right!')
                return
            else:
                print('Sorry, %s isn\'t the right word' % guess)
        print(display_word(word_status))
        tries += 1
        print('%i tries left' % (MAX_TRIES - tries))
    print ('Sorry, you\'ve used up all your tries')
    print('The answer was %s' % word)
    return


if __name__ == '__main__':
    main()
