import math


class fonction:
    def __init__(self, x):
        self.x = x

    def sincos(self):
        sinus = math.sin(self.x ** 2)
        cosinus = math.cos(self.x ** 2)
        return sinus + cosinus

    @staticmethod
    def un():
        return 1

    def egalite(self):
        return self.sincos() == self.un()

def main():
    n = fonction(5)
    print(n.egalite())


if __name__ == '__main__':
    main()