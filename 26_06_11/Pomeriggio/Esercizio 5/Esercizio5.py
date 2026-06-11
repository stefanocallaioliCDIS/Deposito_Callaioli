'''

Classe Cliente
Classe Amministratore
Avrebbero senso con ereditarità da Classe Utente

Classe Articolo
Classe Negozio
'''

class Negozio:
    
    #Costruttore con nome, tipo_cucina, stato di apertura e menu
    def __init__(self, nome:str, inventario):
        self.nome = nome
        self.inventario = inventario                                                #Articoli disponibili
        self.articoliVenduti = []                                                   #Articoli ordinati dai Clienti
        
        self.clienti = []
        self.amministratori = []
        
        self.guadagni=0
        for articolo in self.articoliVenduti:                                       #Calcola guadagni retroattivamente, utile se si vuole rendere passabile articoliVenduti
            self.guadagni+=articolo.prezzo
        
    #metodo per stampare il menu
    def stampaInventario(self):
        print("Inventario", self.nome,":")
        for p in self.inventario:
            print(p)
    
    #metodo per registrare un cliente al negozio     
    def registraCliente(self, nome, password):
        self.clienti.append(Cliente(nome,password))
    
    #metodo per login di un cliente al negozio. Ritorna true se è avvneuto con successo
    def loginCliente(self, nome, password):
        for cliente in self.clienti:
            if cliente.nome==nome:
                if cliente.password==password:
                    print("Login Effettuato")
                    return True
        return False
    
    #metodo per login di un amministratore al negozio. Ritorna true se è avvenuto con successo
    def loginAmministratore(self, nome, password):
        for amministratore in self.amministratori:
            if amministratore.nome==nome:
                if amministratore.password==password:
                    print("Login Effettuato")
                    return True
        return False
    
    
class Articolo:
    
    #Costruttore con nome e prezzo dell'articolo
    def __init__(self, nome:str, quantita:int, prezzo:int):
        self.nome = nome
        self.quantita = quantita
        self.prezzo = prezzo
        
    def __str__(self):
        return (self.nome + " - " + str(self.prezzo)+ " - " + str(self.quantita))
    
class Cliente:
    
    def __init__(self, nome:str, password:str):
            self.nome = nome
            self.password = password
            self.ordine = []                                        #Articoli ordinati dal Cliente

    def __str__(self):
        return (self.nome)
    
    #Cliente può leggere report inventario, si potrebbe migliorare nascondendo la quantità degli articoli
    def reportInventario(self, negozio:str):
        print("Inventario " + negozio.nome +":")
        for articolo in negozio.inventario:
            print (articolo)
    
    #Cliente può acquistare Articoli dal negozio
    def acquista(self,negozio:str, nomeArticolo:str):
        for articolo in negozio.inventario:                         #CHECK DA AGGIUNGERE
            if nomeArticolo==articolo.nome:
                self.ordine.append(articolo)
                negozio.articoliVenduti.append(articolo)
                negozio.guadagni+=articolo.prezzo      

#Classe che gestisce l'inventario e può aggiungere, rimuovere e modificare articoli.            
class Amministratore:
    
    def __init__(self, nome:str, password:str):
            self.nome = nome
            self.password = password
            
    def __str__(self):
        return (self.nome)

    #Queste classi avrebbero bisogno di un check per controllare che l'amministratore lavori al negozio, implemento se ho tempo

    #metodo per aggiungere articoli all'inventario
    def aggiungiAdInventario(self, negozio:Negozio, articolo:Articolo):
        negozio.inventario.append(articolo)
        
    #metodo per rimuovere articoli all'inventario
    def togliDaInventario(self, negozio:Negozio, nome:str):
        rimosso=False
        for articolo in negozio.inventario:
            if articolo.nome == nome:
                negozio.inventario.remove(articolo)
                rimosso=True
        if(rimosso == False):
            print("EROORE: L'articolo non è presente nell'inventario")

    #Amministratore può aggiornare l'inventario                                 #IMPLEMENTARE
    def aggiornaInventario(self, negozio:Negozio, nome:str):
        pass
            
    #Amministratore può leggere report vendite
    def reportVendite(self, negozio):
        print("Report vendite " + negozio.nome +":")
        for articolo in negozio.articoliVenduti:
            print (articolo)
                
    #Amministratore può leggere report inventario
    def reportInventario(self, negozio):
        print("Inventario " + negozio.nome +":")
        for articolo in negozio.inventario:
            print (articolo)


#Aggiungere menù
negozio1 = Negozio ("Nike", [])
articolo1 = Articolo ("Scarpe Blu", 4, 20)
articolo2 = Articolo ("Scarpe Rosse", 10, 30)
articolo3 = Articolo ("Scarpe Verdi", 7, 25)

admin1 = Amministratore("Jace Beleren", "1234")

#admin1.loginAmministratore("Jace Beleren", "1234")

admin1.aggiungiAdInventario(negozio1,articolo1)
admin1.aggiungiAdInventario(negozio1,articolo2)
admin1.aggiungiAdInventario(negozio1,articolo3)

admin1.reportInventario(negozio1)

negozio1.registraCliente("Garruk", "1234")
if (negozio1.loginCliente("Garruk", "1234")):
    print("Benvenuto")


