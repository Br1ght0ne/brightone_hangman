from brightone_hangman.game import Game

if __name__ == '__main__':
    diff = input('Please choose difficulty level ( [E]asy / [M]edium / [H]ard): ').lower()
    game = Game(difficulty=diff)
    game.start()
