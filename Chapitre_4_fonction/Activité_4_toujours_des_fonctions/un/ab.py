class age:
    def __init__(self, age):
        self.age = age
        self.tarif_a = 30
        self.tarif_b = 20
        self.tarif_c = 35

    def reduction(self):
        if self.age <= 10:
            reduc = self.tarif_a * 50 / 100
            return self.tarif_a - reduc
        elif 10 < self.age < 18:
            reduc = self.tarif_b * 30 / 100
            return self.tarif_b - reduc
        elif self.age >= 60:
            reduc = self.tarif_c * 20 / 100
            return self.tarif_c - reduc
        else:
            return self.tarif_c


def montant_total(*x):
    print(f'Prix total a payer: {sum(x)} €')


def main():
    enfant = age(9)
    jumeaux_1 = age(16)
    jumeaux_2 = age(16)
    maman = age(40)
    papa = age(40)

    montant_total(
        enfant.reduction(), jumeaux_1.reduction(), jumeaux_2.reduction(),
        maman.reduction(), papa.reduction()
    )


if __name__ == '__main__':
    main()