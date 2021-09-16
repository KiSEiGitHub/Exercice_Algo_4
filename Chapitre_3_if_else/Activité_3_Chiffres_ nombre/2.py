def main():
    tableau = []

    for i in range(1, 1001):
        i_string = str(i)
        if i_string.endswith('3'):
            i_int = int(i_string)
            tableau.append(i_int)
            if sum(tableau) >= 15:
                print(i)


if __name__ == '__main__':
    main()