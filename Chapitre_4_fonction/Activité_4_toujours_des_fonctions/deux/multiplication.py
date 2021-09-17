import random


class mult:
    def __init__(self, langue):
        self.user = ""
        self.langue = langue
        self.nb_1 = 0
        self.nb_2 = 0
        self.fake_nb_1 = 0
        self.fake_nb_2 = 0

    def table(self):

        swtich = {
            'Anglais': self.awnser,
            'Français': self.reponse
        }

        while True:

            self.nb_1 = random.randint(1, 10)
            self.nb_2 = random.randint(1, 10)
            self.fake_nb_1 = random.randint(1, 100)
            self.fake_nb_2 = random.randint(1, 100)

            print(f'{self.nb_1} * {self.nb_2} ?')
            print(f'{self.fake_nb_1} | {self.fake_nb_2} | {self.nb_1 * self.nb_2}')
            self.user = ""
            while self.user not in [self.fake_nb_1, self.fake_nb_2, self.nb_1 * self.nb_2]:
                self.user = int(input('>> '))

            func = swtich.get(self.langue)
            func()

            print('-' * 50)


    def awnser(self):
        if self.user == self.nb_1 * self.nb_2:
            print('True, you won')
        elif self.user in [self.fake_nb_1, self.fake_nb_2]:
            print('False')
            print(f'The good awnser was {self.nb_1 * self.nb_2}')


    def reponse(self):
        if self.user == self.nb_1 * self.nb_2:
            print('Vrai, tu gagnes')
        elif self.user in [self.fake_nb_1, self.fake_nb_2]:
            print('C\'est faux')
            print(f'La bonne réponse était {self.nb_1 * self.nb_2}')


def main():
    print('Anglais ou Français ?')
    langue = ""
    while langue not in ['Anglais', 'Français']:
        langue = input('>> ')
    mult(langue).table()


if __name__ == '__main__':
    main()