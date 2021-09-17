class division:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def quotient(self):
        return self.a // self.b

    def reste(self):
        return self.a % self.b

    def check(self):
        test_1 = self.reste() < self.b
        test_2 = self.a == self.b * self.quotient() + self.reste()
        return test_1, test_2

    def print(self):
        print(f'Division de {self.a} / {self.b}')
        print(f'Quotient q = {self.quotient()}')
        print(f'Reste r = {self.reste()}')
        verif_r, verif_q = self.check()
        print(f'Vérification reste: {verif_r}')
        print(f'Vérification quotient: {verif_q}')


def main():
    a = division(100, 7)
    a.print()


if __name__ == '__main__':
    main()