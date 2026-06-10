#Esercizio 2: Crea classe Libro con metodi descritti

'''
#Restituisce False se l'utente vuole uscire, True altrimenti. Necessita di string per il messaggio di input
def checkRepeat(message:str):
    scelta = input(message)
    if scelta == "no":                                             
        return False
    else:
        return True
'''

class Libro:

    def __init__(self, titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine
        
    #metodo che stampa una descrizione del libro
    def descrizione(self):
        print("Il libro", self.titolo,"è stato scritto da", self.autore, "e ha", self.pagine,"pagine")

        
libro1 = Libro("Il colore della Magia", "Terry Pratchet", 310)
libro1.descrizione()

'''
repeat = True
while repeat:
    
    repeat = checkRepeat("Vuoi continuare ad aggiungere libri?\n")           #Check di uscita    
'''

