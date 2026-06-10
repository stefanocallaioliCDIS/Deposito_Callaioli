#dunder methods (double under __), metodi SPECIALI che esistono anche quando non definiti, possono essere sovrascitti

class Squadra:

    def __init__(self, nome, giocatori):

        self.nome = nome

        self.giocatori = giocatori
        
    #__str__ - metodo che definisce cosa fare quando l'istanza viene trattata come stringa
    def __str__(self):                                  #toString()
        return self.nome
    
    #__len__ - metodo che definisce cosa fare quando len() viene chiamato sull'istanza
    def __len__(self):
        return len(self.giocatori)
    
    #__call__ - metodo che definisce cosa fare quando l'istanza è usata come funzione
    def __call__(self):
        pass #Esempio sotto

    #__eq__ - metodo che definisce cosa fare quando == viene usato sull'istanza (Esistono dunder methods anche per altri operatori)
    def __eq__(self,altro):
        return self.nome==altro.nome and self.giocatori == altro.giocatori

squadra1 = Squadra("Tigri", ["Luca", "Marco", "Anna"])
squadra2 = Squadra("Tigri", ["Luca", "Marco", "Anna"])

print(squadra1)
print(len(squadra1))
#squadra1(10)
print(squadra1 == squadra2)


#Esempio __call__
class Moltiplicatore:

 def __init__(self, numero):

    self.numero = numero

 def __call__(self, valore):

    return valore * self.numero


doppio = Moltiplicatore(2)

print(doppio(10))