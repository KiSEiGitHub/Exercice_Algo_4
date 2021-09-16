import math

class triangle:
    def __init__(self, ab, bc, ac):
        self.ab = ab
        self.bc = bc
        self.ac = ac
    
    def Existence(self):
        return 'yes' if self.ab + self.bc >= self.ac else 'no'

    def rectangle(self):
        return 'yes' if self.bc ** 2 + self.ac ** 2 == self.ab ** 2 else 'no'
    
    def equilateral(self):
        return 'yes' if self.ab == self.bc == self.ac else 'no'
    
    def isocele(self):
        return 'yes' if self.ab == self.ac and self.ac != self.bc else 'no'
    
    def angle_aigue(self):
        cos_a = math.cos(-self.ab ** 2 + self.bc ** 2 + self.ac ** 2 / 2 * self.bc)
        return 'yes' if cos_a >= 0 else 'no'
    
    @staticmethod
    def test(iso, equi, rec, angle, exi):
        print(f'Triangle existant: {exi}')
        print(f'Triangle rectangle: {rec}')
        print(f'Triangle équitaléral: {equi}')
        print(f'Triangle isocèle: {iso}')
        print(f'Angle aigue: {angle}')
        print('-' * 50)

def main():
    while True:
        a = int(input('AB: '))
        b = int(input('BC: '))
        c = int(input('AC: '))
        coord = triangle(a, b, c)
        coord.test(coord.isocele(), coord.equilateral(),
               coord.rectangle(), coord.angle_aigue(), coord.Existence())

if __name__ == '__main__':
    main()