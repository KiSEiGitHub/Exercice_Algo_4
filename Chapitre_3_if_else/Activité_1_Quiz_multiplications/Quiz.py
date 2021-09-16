import random


def main():
    a = random.randint(1, 10)
    b = random.randint(1, 10)

    print(f'{a} * {b} ?')
    user_choice = int(input('>> '))

    if user_choice == a * b:
        print(f'Bravo c\'était {user_choice}')
    else:
        print(f'Dommage... c\'était {a * b}')

if __name__ == '__main__':
    main()