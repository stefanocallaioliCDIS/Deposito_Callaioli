#Esercizio 2
#Crea una classe Animale con un attributo di classe numeroAnimali che incrementa ogni volta che viene creata un'istanza

class Animale:
    numeroAnimali=0
    
    def __init__(self, nome, specie):
        self.nome = nome
        self.specie = specie
        Animale.numeroAnimali+=1
        
    @classmethod
    def quantiAnimali(cls):
        print("Numero di animali creati:", cls.numeroAnimali)
        
#Crea 3 animali
Animale("Oliver", "Gatto")
Animale("Zoe", "Cane")
Animale("Poldo", "Cane")

#Chiamiamo il class method
Animale.quantiAnimali()             #Output - Numero di animali creati: 3

