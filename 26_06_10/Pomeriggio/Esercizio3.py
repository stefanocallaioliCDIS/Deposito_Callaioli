#Esercizio 3
#Crea una classe ContoCorrente con i metodi descritti
#Extra: Rendalo replicabile su più conti

class ContoCorrente:
    
    #costruttore
    def __init__(self, intestatario:str, saldo:int=0):
        self.intestatario = intestatario
        self.saldo = saldo
    
    #stampa ContoCorrente
    def stampaSaldo(self):
        print(self.intestatario, ": ", self.saldo, "€" )
        
    #deposita importo nel ContoCorrente
    def deposito(self, importo:int):
        if(importo<=0):
            print("ERRORE: importo minore o uguale a 0 ")
        else:
            self.saldo+=importo
            
    #preleva importo da ContoCorrente
    def preleva(self, importo:int):
        if(importo>self.saldo):
            print("ERRORE: importo maggiore del saldo disponibile ")
        else:
            self.saldo-=importo
            

contoCorrente1 = ContoCorrente("Mario", 200)
contoCorrente2 = ContoCorrente("Luigi")
contoCorrenti= [contoCorrente1, contoCorrente2]

repeat = True
while repeat:
    
    for conto in contoCorrenti:
        conto.stampaSaldo()
    sceltaConto = int(input("A quale conto vuoi accedere?\n"))-1

    print("1. Deposito\n2. Prelievo\n3. Esci")
    option = input("Quale comando vuoi eseguire?\n")                    #Menù per scegliere la funzione da eseguire

    match option:
        case "1":
            importo = int(input("Importo: "))                           
            contoCorrenti[sceltaConto].deposito(importo)
        case "2":
            importo = int(input("Importo:"))
            contoCorrenti[sceltaConto].preleva(importo)   
        case "3":                                                       #Controllo uscita
            repeat=False                   
        case _:                             
            print ("Comando non valido")
            
    print("-----------------------")

    