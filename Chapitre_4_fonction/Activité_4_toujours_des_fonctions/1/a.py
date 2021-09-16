def reduction(age):

    billet = 40

    if age <= 10:
        remise = billet * 50 / 100
        return billet - remise
    elif 10 < age < 18:
        remise = billet * 30 / 100
        return billet - remise
    elif age >= 60:
        remise = billet * 20 / 100
        return billet - remise
    else:
        return 18


def main():
    age = int(input('age: '))
    prix = reduction(age)
    print(f'prix du billet: {round(prix, 2)} €')


if __name__ == '__main__':
    main()