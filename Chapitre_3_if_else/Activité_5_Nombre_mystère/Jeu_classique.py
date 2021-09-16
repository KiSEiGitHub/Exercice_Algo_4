import random

class Game:
    def __init__(self, user, nb):
        self.user = user
        self.nb = nb
    
    def game(self):
        if self.user == self.nb:
            print('Trouvé')
        elif self.user > self.nb:
            print('moins')
        elif self.user < self.nb:
            print('plus')

def main():
    nb_mystere = random.randint(1, 100)
    user_choice = 2

    print('Nombre mystère entre 1 et 100')


    while user_choice != nb_mystere:
        user_choice = int(input('>> '))
        game = Game(user_choice, nb_mystere)
        game.game()


if __name__ == '__main__':
    main()