'''
1.2 Feladat
Készíts egy programot, amelyben van egy Negyzet nevű osztály. Attribútuma legyen az oldal hossza. 
A metódus ne a kerület- illetve a területértékkel térjen vissza, hanem maga gondoskodjon ezen értékek kiírásáról egy egész mondatos formában.
'''

class Negyzet:
    def __init__(self, oldalhossz):
        self.oldalhossz = oldalhossz
    def valami(self):
        return (f'A negyzet kerulete:', self.oldalhossz ** 2, 'a negyzet kerulete: ',self.oldalhossz * 4)

negyzet01 = Negyzet(2)
print(negyzet01.valami())