import math


class calcul:
    def __init__(self, longeur, rayon, base, hauteur, largeur):
        self.longeur = longeur
        self.rayon = rayon
        self.base = base,
        self.hauteur = hauteur
        self.largeur = largeur

    def volume_cube(self):
        return self.longeur ** 3

    def volume_boule(self):
        return 4 * math.pi * self.rayon ** 2

    def volume_cylindre(self):
        return math.pi * self.rayon ** 2

    def volume_para(self):
        return self.longeur * self.largeur * self.hauteur

    @staticmethod
    def affich(cube, boule, cylindre, para):
        print(f'Volume cube: {round(cube, 2)} cm³')
        print(f'Volume boucle: {round(boule, 2)} cm³')
        print(f'Volume cylindre: {round(cylindre, 2)} cm³')
        print(f'Volume para: {round(para, 2)} cm³')

def main():
    vol = calcul(9, 2, 4, 3, 5)
    vol.affich(vol.volume_cube(), vol.volume_boule(), vol.volume_cylindre(), vol.volume_para())


if __name__ == '__main__':
    main()