'''
Esercizio: Sistema di Gestione Negozio
Lo scopo di questo esercizio è implementare un sistema di gestione per un negozio che deve
interagire con clienti, gestire l'inventario e permettere agli amministratori di
supervisionare le operazioni. Il sistema sarà strutturato in tre parti principali:
1.Gestione Clienti:
I clienti possono visualizzare gli articoli disponibili in inventario.
I clienti possono selezionare e acquistare articoli dall'inventario.
Il sistema tiene traccia degli acquisti dei clienti.
2.Gestione dell'Inventario:
Gli articoli in magazzino sono elencati con il nome, il prezzo e la quantità.
È possibile aggiungere nuovi articoli all'inventario.
Gli articoli possono essere rimossi o aggiornati (ad es., cambiare prezzo o
quantità).
3.Amministrazione:
Gli amministratori possono visualizzare un rapporto delle vendite.
Gli amministratori possono visualizzare lo stato corrente dell'inventario.
Il sistema tiene traccia dei guadagni totali.
Puoi pre inserire gli amministratori non i clienti
Il sistema dovrebbe permettere di simulare un'interazione base tra il cliente e il negozio
dopo un login e una registrazione, nonché fornire gli strumenti necessari per la
manutenzione e l'analisi del negozio da parte degli amministratori.
'''

'''
Extra: Più di un negozio può essere gestito, come se fosse un sito che vende merce da più posti
'''

'''
Altre cose che avrei voluto implementare
- In articoliVenduti salvare anche chi ha comprato l'articolo con un tupla
- Check in metodo acquista
- Classe Sito
- Implementare modificaArticolo
- Dizionari per utenti?
- Menù ripetibile
'''

class Negozio:
    
    #Costruttore con nome, tipo_cucina, stato di apertura e menu
    def __init__(self, nome:str, inventario):
        self.nome = nome
        self.inventario = inventario                                                #Articoli disponibili
        self.articoliVenduti = []                                                   #Articoli venduti ai Clienti
        
        self.clienti = []                                                           #Lista dei clienti registrati del negozio
        self.amministratori = []                                                    #Lista degli admin del negozio
        
        self.guadagni=0
        for articolo in self.articoliVenduti:                                       #Calcola guadagni retroattivamente, utile se si vuole rendere passabile articoliVenduti
            self.guadagni+=articolo.prezzo
        
    def __str__(self):
        return self.nome
    
    #metodo per stampare il menu
    def stampaInventario(self):
        print("Inventario", self.nome,":")
        for p in self.inventario:
            print(p)
    
    #metodo per registrare un cliente al negozio     
    def registraCliente(self, nome, password):
        cliente = Cliente(nome,password)
        self.clienti.append(cliente)
        return cliente
    
    #metodo per login di un cliente al negozio. Ritorna il cliente se è avvneuto con successo
    def loginCliente(self, nome, password):
        for cliente in self.clienti:
            if cliente.nome==nome:
                if cliente.password==password:
                    return cliente
        return False
    
    #metodo per login di un amministratore al negozio. Ritorna l'amministratore se è avvenuto con successo
    def loginAmministratore(self, nome, password):
        for amministratore in self.amministratori:
            if amministratore.nome==nome:
                if amministratore.password==password:
                    return amministratore
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
            self.ordine = []                                        #Articoli comprati dal Cliente

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
                articolo.quantita-=1

#Classe che gestisce l'inventario e può aggiungere, rimuovere e modificare articoli.            
class Amministratore:
    
    def __init__(self, nome:str, password:str):
            self.nome = nome
            self.password = password
            
    def __str__(self):
        return (self.nome)

    #Queste classi avrebbero bisogno di un check per controllare che l'amministratore lavori al negozio, ma come usate nel menu non dovrebbero dare errori, implemento se ho tempo

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


#Popoliamo negozi
negozio1 = Negozio ("Nike", [])
negozi = [negozio1]

#Popoliamo utenti
admin1 = Amministratore("Jace Beleren", "1234")
negozio1.amministratori.append(admin1)
#negozio1.registraCliente("Garruk", "1234")  #Non permesso dalla traccia

#Popoliamo inventario
articolo1 = Articolo ("Scarpe Blu", 4, 20)
articolo2 = Articolo ("Scarpe Rosse", 10, 30)
articolo3 = Articolo ("Scarpe Verdi", 7, 25)
articolo4 = Articolo ("Scarpe Bianche", 2, 50)
articolo5 = Articolo ("Scarpe Nere", 1, 24)
negozio1.loginAmministratore("Jace Beleren", "1234")
admin1.aggiungiAdInventario(negozio1,articolo1)
admin1.aggiungiAdInventario(negozio1,articolo2)
admin1.aggiungiAdInventario(negozio1,articolo3)
admin1.aggiungiAdInventario(negozio1,articolo4)
admin1.aggiungiAdInventario(negozio1,articolo5)


#negozioAttuale
#utenteAttuale


#SCELTA DEL NEGOZIO
c=1
for negozio in negozi:
    print(str(c) + ". " + str(negozio))
negozioAttuale = None
while (negozioAttuale == None):
    nomeNegozio = input("Come si chiama il negozio a cui vuoi accedere?\n")
    for negozio in negozi:
        if negozio.nome == nomeNegozio:
            negozioAttuale = negozio
        else:
            print("Questo negozio non esiste!")
            
#SCELTA: LOGIN O REGISTRAZIONE AL NEGOZIO?
option = input("Cosa vuoi fare?\n1. Login come cliente\n2. Registrazione come cliente\n3. Login come amministratore\n")

utenteAttuale=None
nome = input("Inserisci il tuo nome:\n")
password = input("Inserisci la tua password:\n")

match option:
    case "1":
        if negozioAttuale.loginCliente(nome,password):
            utenteAttuale=negozioAttuale.loginCliente(nome,password)                    #Brutto, da sistemare se c'è tempo
            print("Login Effettuato. Buongiorno "+utenteAttuale.nome+"!")
        else:
            print("ERRORE: Questo utente non esiste o la password non è corretta.")
    case "2":
        utenteAttuale=negozioAttuale.registraCliente(nome,password)
        print("Registrazione Effettuata. Buongiorno "+utenteAttuale.nome+"!")
    case "3":
        if negozioAttuale.loginAmministratore(nome,password):
            utenteAttuale=negozioAttuale.loginAmministratore(nome,password)             #Brutto, da sistemare se c'è tempo
            print("Login Effettuato. Buongiorno Admin "+utenteAttuale.nome+"!")

#MENU DEL CLIENTE
if type(utenteAttuale) is Cliente:
    articolo = None
    while articolo != "ESCI":
        utenteAttuale.reportInventario(negozioAttuale)
        articolo = input("Cosa vuoi comprare? Scrivi ESCI per uscire\n")
        if articolo == "ESCI":
            print("Arrivederci "+utenteAttuale.nome+"!")
            break
        else:
            utenteAttuale.acquista(negozioAttuale, articolo)
    
#MENU DELL'AMMINISTRATORE   
elif type(utenteAttuale) is Amministratore:
    option = None
    while option != "4":
        utenteAttuale.reportInventario(negozioAttuale)
        option = input("Cosa vuoi fare?\n1. Visualizza rapporto vendite\n2. Aggiungi un articolo\n3. Rimuovi un articolo\n4. Esci\n")
        match option:
            case "1":
                utenteAttuale.reportVendite(negozioAttuale)
            case "2":
                nomeArticolo = input("Nome: ")
                prezzoArticolo = input("Prezzo: ")
                quantitaArticolo = input("Quantita: ")
                utenteAttuale.aggiungiAdInventario(negozioAttuale,Articolo(nomeArticolo, prezzoArticolo, quantitaArticolo))
                print (nomeArticolo + " aggiunto all'inventario!")
            case "3":
                utenteAttuale.reportInventario(negozioAttuale)
                nomeArticolo = input("Nome: ")
                utenteAttuale.togliDaInventario(negozioAttuale, nomeArticolo)
                print (nomeArticolo + " rimosso dall'inventario!")
                
            case "4":
                print("Arrivederci "+utenteAttuale.nome+"!")
                break
else:
    print ("ERRORE: Utente invalido")
    #break
utenteAttuale = None
negozioAttuale = None

