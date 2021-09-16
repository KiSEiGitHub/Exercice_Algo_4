def table(y):
    for i in range(1, 11):
        print(f'{y} * {i} = {y * i}')
    print('-' * 50)

def main():
    while True:
        a = int(input('Table: '))
        table(a)

if __name__ == '__main__':
    main()