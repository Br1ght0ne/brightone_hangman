"""
Play Hangman!
"""

from random import choice
from sys import exit
import os
from string import ascii_letters


from brightone_hangman.man import Man


class Game:
    def __init__(self, difficulty='e'):
        self._dictionary = self._build_dictionary(difficulty)
        self.word = choice(self._dictionary).strip()
        self.guessed = ['_'] * len(self.word)
        self.guesses_made = 0
        self.man = Man()
        self.tried = []

    @staticmethod
    def _best_guess(word):
        return len(set(word))

    @staticmethod
    def _build_dictionary(diff):
        dirname = os.path.dirname(os.path.realpath(__file__))
        d = {
            'e': 'easy',
            'm': 'medium',
            'h': 'hard'
        }
        if diff[0] not in d.keys():
            return None
        with open(dirname + '/' + d[diff[0]], 'r') as f:
            return [word.upper() for word in f.readlines()]

    @staticmethod
    def _explain_rules():
        return '\n'.join(['The rules are simple:',
                          '\t1. Make guesses ONE letter long.',
                          '\t2. Enter "quit" to end game.'])

    def _exit(self, return_code: int):
        print(f'The word was {self.word}, and you could get it in {self._best_guess(self.word)} guesses.',
              sep='\n')
        exit(return_code)

    def print_status(self):
        def print_man():
            print('',
                  self.man,
                  '',
                  sep='\n')
        print('',
              ' '.join(self.guessed) + f'\tGuesses: {self.guesses_made}' + f'\tTried letters: {"".join(self.tried)}',
              '',
              sep='\n')
        print_man()

    def start(self):
        print('Welcome to Hangman!',
              '',
              self._explain_rules(),
              '',
              'Let\'s start!',
              '',
              'I have prepared a word for you. Let\'s see...',
              f'It is {len(self.word)} letters long!',
              sep='\n')
        self.print_status()
        while True:
            try:
                user_guess = input('Make your guess by typing a letter: ').upper()
            except KeyboardInterrupt:
                print()
                self._exit(1)
            if len(user_guess) > 1:
                if user_guess == 'QUIT':
                    self._exit(0)
                else:
                    print('Please enter only ONE letter at a time.')
            else:
                if user_guess in self.tried:
                    print('You already tried this letter.')
                elif user_guess not in ascii_letters:
                    print('This is not a letter.')
                else:
                    self.guesses_made += 1
                    if user_guess in self.word:
                        print('Congrats! You guessed a letter!')
                        for index, letter in enumerate(self.word):
                            if user_guess == letter:
                                self.guessed[index] = letter
                        if all([x != '_' for x in self.guessed]):
                            print('You win!',
                                  f'You took {self.guesses_made} guesses '
                                  + f'with a minimum of {self._best_guess(self.word)}.',
                                  sep='\n')
                            break
                    else:
                        if not self.man.add_limb():
                            print('You lose :(')
                            self._exit(0)
                        print('You didn\'t get it this time. Try again!')
                        self.tried.append(user_guess)
                    self.print_status()
