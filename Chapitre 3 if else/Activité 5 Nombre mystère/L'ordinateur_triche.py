import random


class Game:
    def __init__(self, nb):
        self.user = ""
        self.nb = nb
        self.triche = 0
        self.essaie = 0

    def game(self):
        while True:
            self.user = int(input('>> '))

            if self.user == self.nb:
                print('Trouvé')
                print(f'il a tricher {self.triche} fois')
                print(f'Vous avez trouvé en {self.essaie} essaies')
                break

            elif self.user > self.nb:
                triche = random.randint(1, 4)
                if triche == 2:
                    print('moins')
                    ajout = random.randint(-3, 3)
                    self.nb += ajout
                    self.triche += 1
                else:
                    print('moins')
                self.essaie += 1

            elif self.user < self.nb:
                triche = random.randint(1, 4)
                if triche == 2:
                    print('plus')
                    ajout = random.randint(-3, 3)
                    self.nb += ajout
                    self.triche += 1
                else:
                    print('plus')

                self.essaie += 1


def main():

    nb_mystere = random.randint(1, 20)
    print('Nombre mystère entre 1 et 100')

    game = Game(nb_mystere)
    game.game()


if __name__ == '__main__':
    main()
