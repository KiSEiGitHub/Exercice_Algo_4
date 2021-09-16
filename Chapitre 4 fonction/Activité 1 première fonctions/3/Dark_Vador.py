def demande_prenom(x, y):
    prenom = x
    nom = y.upper()
    return prenom, nom

def main():
    a = input('Prénom: ')
    b = input('Nom: ')

    first_name, last_name = demande_prenom(a, b)

    print(f'{first_name} {last_name}')


if __name__ == '__main__':
    main()