class calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def F1(self):
        return self.a ** 2 + self.b ** 2

    def F2(self):
        return self.a ** 2 + 2 * self.a * self.b + self.b ** 2

    def egalite(self):
        return self.F1() == self.F2()

    def FC1(self):
        return self.a ** 3 - 3 * self.a ** 2 * self.b - 3 * self.a * self.b ** 2 + self.b ** 3

    def FC2(self):
        return self.a ** 3 - 3 * self.a ** 2 * self.b + 3 * self.a * self.b ** 2 - self.b ** 3

    def egalite2(self):
        return self.FC2() == self.F1()

def main():
    number = calc(8, 8)
    print(number.egalite2())


if __name__ == '__main__':
    main()