#Esercizio 3
#Creare una classe Ristorante e Piatto con metodi come descritti
#Extra: implementare Cliente (Svolto)
#Extra: implementare Chef (Non Svolto)

class Ristorante:
    
    #Costruttore con nome, tipo_cucina, stato di apertura e menu
    def __init__(self, nome:str, tipo_cucina:str):
        self.nome = nome
        self.tipo_cucina = tipo_cucina
        self.aperto = False
        self.menu = []                                              #Menu del ristorante
        self.piattiOrdinati = []                                    #Piatti ordinati dai Clienti
        
    #metodo che stampa una descrizione del ristorante
    def descriviRistorante(self):
        print(self.nome,", un ristorante che serve cucina di tipo", self.tipo_cucina)
    
    #metodo che stampa lo stato di apertura del ristorante
    def statoApertura(self):
        if self.aperto:
            print(self.nome, "è attualmente aperto!")
        else:
            print(self.nome, "è attualmente chiuso.")
    
    #metodo che apre il ristorante
    def apriRistorante(self):
        self.aperto = True
        print(self.nome, "è ora aperto!")
    
    #metodo che chiude il ristorante
    def chiudiRistorante(self):
        self.aperto = False
        print(self.nome, "è ora chiuso.")
    
    #metodo per aggiungere piatti al menu
    def aggiungiAlMenu(self, piatto:Piatto):
        self.menu.append(piatto)
        
    #metodo per rimuovere piatti dal menu
    def togliDalMenu(self, piatto:Piatto):
        self.menu.remove(piatto)
    
    #metodo per stampare il menu
    def stampaMenu(self):
        print("Menu", self.nome,":")
        for p in self.menu:
            print(p)
    
class Piatto:
    
    #Costruttore con nome e prezzo del piatto
    def __init__(self, nome:str, prezzo:int):
        self.nome = nome
        self.prezzo = prezzo
        
    def __str__(self):
        return (self.nome + " - " + str(self.prezzo))
    
class Cliente:
    
    def __init__(self, nome:str, saldo:int):
            self.nome = nome
            self.saldo = saldo
            self.ordine = []                                        #Piatti ordinati dal Cliente

    def ordinaPiatto(self, ristorante, piatto):
        if ristorante.aperto == False:                              #Check che il ristorante sia aperto
            print("ERRORE: Il ristorante è chiuso")
        elif piatto not in ristorante.menu:                         #Check che il piatto esista nel menu
            print("ERRORE: Il piatto non è nel menù")
        elif(piatto.prezzo>self.saldo):                             #Check che il cliente possa pagare il piatto
            print("ERRORE: Il cliente non può pagare il piatto")
        else:
            ristorante.piattiOrdinati.append(piatto)
            self.ordine.append(piatto)
            self.saldo -= piatto.prezzo
            print(self.nome,"ha ordinato",piatto.nome,"da",ristorante.nome)
            
    def __str__(self):
        return (self.nome + " - " + str(self.saldo))
        
        
   
ristorante1 = Ristorante("Sakura Ya", "Giapponese")
piatto1 = Piatto("Uramaki", 20)
piatto2 = Piatto("Nigiri", 10)
piatto3 = Piatto("Samurai Stick", 5)

#Test metodi 
ristorante1.descriviRistorante()
print()
ristorante1.apriRistorante()
print()
ristorante1.chiudiRistorante()
print()
ristorante1.aggiungiAlMenu(piatto1)
ristorante1.aggiungiAlMenu(piatto2)
ristorante1.aggiungiAlMenu(piatto3)
ristorante1.stampaMenu()
print()
ristorante1.togliDalMenu(piatto2)
ristorante1.stampaMenu()
print()
'''
Sakura Ya , un ristorante che serve cucina di tipo Giapponese

Sakura Ya è ora aperto!

Sakura Ya è ora chiuso.

Menu Sakura Ya :
Uramaki - 20
Nigiri - 10
Samurai Stick - 5

Menu Sakura Ya :
Uramaki - 20
Samurai Stick - 5
'''

cliente1=Cliente("Mario Rossi", 100)
print(cliente1)
cliente1.ordinaPiatto(ristorante1, piatto1)
print(cliente1)
ristorante1.apriRistorante()
cliente1.ordinaPiatto(ristorante1, piatto1)
print(cliente1)
'''
Mario Rossi - 100
ERRORE: Il ristorante è chiuso
Mario Rossi - 100
Sakura Ya è ora aperto!
Mario Rossi ha ordinato Uramaki da Sakura Ya
Mario Rossi - 80
'''

