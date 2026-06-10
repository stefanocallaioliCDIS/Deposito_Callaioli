
#Classe: Schema astratto / modello logico che descrive gli oggetti che possono derivare da essa 
#Oggetti: istanza reale della classe

#cosa definisce la classe?
#metodi (speciali e non)
#tipo dell'oggetto
#caratteristiche/attributi

#Gli oggetti che derivano da una stessa classe non condividono
#il valore attributi
#come usa metodi
#nome proprio

#Dichiarazione/Definizione della classe
class Automobile:                                   #classe usata per creare oggetti di tipo Automobile
    
    numero_di_ruote = 4
    
    #Costruttore (definisce attributi necessari per la creazione della classe)
    def __init__(self, marca, modello):             #__init__ dunder method (double under __), metodi speciali che esistono anche quando non definiti
        
        #attributi
        self.marca = marca                          #self, modo per rifersi all'oggetto stesso all'interno della dichiarazione della classe
        
        self.modello = modello
    
    def stampa_info(self):
        
        print("L'automobile è una", self.marca, self.modello)


#Istanziazione della classe
auto1 = Automobile("Fiat", "500") #Chiamata del costruttore
auto2 = Automobile("BMW","X3")

auto1.stampa_info()
auto2.stampa_info()

#--------------------------------------------
#tipi di metodi
#metodi di istanza - operano su un'istanza specifica, l'oggetto stesso, implementato passando self
#metodi di classe - metodi di classe, operano implementato con @classmethod e passando cls
#metodi statici - non opera su istanze della classe o la classe stessa, implementato con @staticmethod

#metodi di istanza
class Persona:
    def __init__(self, nome, eta):
        self.nome = nome
        self. eta = eta
    
    def saluta(self):
        print(f"Ciao, mi chiamo {self.nome}")
        
p = Persona("Pippo",30)

print(p.nome)
print(p.eta)

#metodi statici
class Calcolatrice:
    
    @staticmethod
    def somma(a, b):
        return a + b
    
risultato = Calcolatrice.somma(5, 3)

#metodi di classe
class Contatore:
    numero_istanze=0
    
    def __init__(self):
        Contatore.numero_istanze += 1
        self.numero_istanze += 1
        
    @classmethod
    def mostra_numero_istanze(cls):
        print(f"Sono state create {cls.numero_istanze} istanze.")
        
c1 = Contatore()
c2 = Contatore()
c3 = Contatore()
    
print(c1.numero_istanze)
print(c2.numero_istanze)
print(c3.numero_istanze)
Contatore.mostra_numero_istanze()
    
    