def table(x):
    for i in range(1, 11):
        print(f'{x} * {i} = {x * i}')
    print('-' * 50)

def main():
    while True:
        a = int(input('Table: '))
        table(a)

if __name__ == '__main__':
    main()