#Esercizio 1
#Crea una Classe Convertitore con 2 metodi statici: 1 che converte km in miglia e 1 che converte € in $

class Convertitore:
    
    #costanti per la conversione
    EURODOLLARIRATIO=1.08
    KMMIGLIARATIO=0.62137

    #Costruttore per decidere che tipo di Convertitore vogliamo creare
    def __init__(self,tipoConversione:str):
        self.tipoConversione=tipoConversione

    def __call__(self, valore:int):
        if (self.tipoConversione=="km miglia"):
            return Convertitore.kmToMiglia(valore)
        elif(self.tipoConversione=="euro dollari"):
            return Convertitore.euroToDollari(valore)

    #implementazione con metodi statici
    @staticmethod
    def euroToDollari(euro:int):
        return euro*Convertitore.EURODOLLARIRATIO
    
    @staticmethod
    def kmToMiglia(km:int):
        return km*Convertitore.KMMIGLIARATIO
  

      

km=100
euro=100

#Esempio con metodi statici
print("Conversione da", km, "km a miglia:", Convertitore.kmToMiglia(km))
print("Conversione da", euro, "€ a $:", Convertitore.euroToDollari(euro),"\n")

#Esempio con oggetto Convertitore
kmMiglia = Convertitore("km miglia")
euroDollari = Convertitore("euro dollari")
print("Conversione da", km, "km a miglia:", kmMiglia(km))
print("Conversione da", euro, "€ a $:", euroDollari(euro),"\n")
