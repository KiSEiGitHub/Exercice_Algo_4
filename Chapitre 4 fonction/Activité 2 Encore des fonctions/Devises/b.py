def conversion_euros(montant, devise):
    swtich = {
        'dollars': f'{montant * 1.17} $',
        'livre': f'{montant * 0.85} livres',
        'yen': f'{montant * 128.76} yen'
    }

    print(swtich.get(devise))

def main():
    a = float(input('Euro: '))
    b = input('divise: ')
    conversion_euros(a, b)


if __name__ == '__main__':
    main()