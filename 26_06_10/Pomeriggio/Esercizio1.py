#Esercizio 1: Crea classe Punto con metodi descritti
from math import sqrt

class Punto:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    #metodo che muove il punto
    def muovi(self, x, y):
        self.x = x
        self.y = y
    #metodo che calcola la distanza dall'origine
    def distanzaDaOrigine(self):
        print(sqrt(self.x**2 + self.y**2))
        
punto1 = Punto(1, 2)
punto2 = Punto(0, 0)

print(punto1.x, punto1.y)
print(punto2.x, punto2.y)

punto2.muovi(3, 3)

print(punto1.x, punto1.y)
print(punto2.x, punto2.y)

punto1.distanzaDaOrigine()
punto2.distanzaDaOrigine()
