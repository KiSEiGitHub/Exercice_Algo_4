import math


class calc:
    def __init__(self, a, b, longeur, largeur, rayon):
        self.a = a
        self.b = b
        self.longeur = longeur
        self.largeur = largeur
        self.rayon = rayon

    def peri_rec(self):
        return 2 * self.a + 2 * self.b

    def aire_rec(self):
        return self.longeur * self.largeur

    def peri_disque(self):
        return 2 * math.pi * self.rayon

    def aire_disque(self):
        return math.pi * self.rayon ** 2

    @staticmethod
    def affich(peri_rec, aire_rec, peri_disque, aire_disque):
        print(f'Périmètre rectangle = {round(peri_rec, 2)}')
        print(f'Aire rectangle = {round(aire_rec, 2)}')
        print(f'Périmètre disque = {round(peri_disque, 2)}')
        print(f'Aire disque = {round(aire_disque, 2)}')

def main():
    a = calc(5, 2, 8, 6, 8)
    a.affich(
        a.peri_rec(), a.aire_rec(),
        a.peri_disque(), a.aire_disque()
    )

if __name__ == '__main__':
    main()