import random


class Game:
    def __init__(self, nb):
        self.user = ""
        self.nb = nb
        self.ment = 0
        self.essaie = 0

    def game(self):
        while True:
            self.user = int(input('>> '))

            if self.user == self.nb:
                print('Trouvé')
                print(f'il a menti {self.ment} fois')
                print(f'Vous avez trouvé en {self.essaie} essaies')
                break

            elif self.user > self.nb:
                ment = random.randint(1, 4)
                if ment == 2:
                    print('plus')
                    self.ment += 1
                else:
                    print('moins')
                self.essaie += 1

            elif self.user < self.nb:
                ment = random.randint(1, 4)
                if ment == 2:
                    print('moins')
                    self.ment += 1
                else:
                    print('plus')

                self.essaie += 1


def main():

    nb_mystere = random.randint(1, 2)
    print('Nombre mystère entre 1 et 100')

    game = Game(nb_mystere)
    game.game()


if __name__ == '__main__':
    main()
