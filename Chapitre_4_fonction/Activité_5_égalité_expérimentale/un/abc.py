import math


class calcul:
    def __init__(self, x):
        self.x = x

    def valeur_absolue(self):
        return self.x if self.x > 0 else 'pas ok'

    def racine_carre(self):
        return math.sqrt(self.x ** 2)

    def fg(self):
        return self.racine_carre() == self.valeur_absolue()


def main():
    a = calcul(9)
    print(a.fg())

if __name__ == '__main__':
    main()