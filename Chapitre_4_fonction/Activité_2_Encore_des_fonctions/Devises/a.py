def conversion_euros_vers_dollars(montant):
    return montant * 1.17

def main():
    a = float(input('euro: '))
    dollars = conversion_euros_vers_dollars(a)
    print(f'{round(dollars, 2)} $')


if __name__ == '__main__':
    main()