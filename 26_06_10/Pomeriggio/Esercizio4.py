#Esercizio 4
#Crea una classe Garage con i metodi descritti
#Extra 1: Crea anche una classe Auto (Svolto)
#Extra 2: Inserisci un controllo di validità delle targhe (Non svolto)

class Auto:

    #costruttore
    def __init__(self, targa:str):
        self.targa = targa
    
    #targa è l'unico attributo che identifica Auto
    def __str__(self):
        return self.targa
    def __eq__(self, altro):
        return self.targa == altro.targa
    
class Garage:
    
    #costruttore
    def __init__(self, capienza:int, autoPresenti):
        self.maxCapienza = capienza
        self.capienza = capienza - len(autoPresenti)
        self.autoPresenti = autoPresenti
    
    def __str__(self):
        garageString=""
        for a in self.autoPresenti:
            garageString+=str(a)+" "                    #Casti per renderlo una string, utilizzando __str__ di Auto
        return garageString
            
    #metodo parcheggia
    def parcheggia(self, targa:str):
        if self.capienza<=0:                            #Check capienza
            print("ERRORE: Garage pieno")
        else:
            nonPresente = True
            for a in self.autoPresenti:
                if a.targa==targa:                      #Check auto già presente
                    print("ERRORE: Auto già presente")
                    nonPresente = False
                    break
            if nonPresente:                             #Check passati, possiamo parcheggiare l'auto
                self.autoPresenti.append(Auto(targa))
                self.capienza-=1
    
    def rimuovi(self, targa:str):
        trovato = False
        for a in self.autoPresenti:                     #Check auto presente
            if (a.targa==targa):                        #Trovata auto, possiamo rimuovere
                self.autoPresenti.remove(a)
                trovato = True
                self.capienza+=1
                break
        if trovato == False:                            #Arrivati in fondo con auto non trovata, errore
            print("ERRORE: Auto non trovata")
                
    
    def postiliberi(self):
        return self.capienza                            #Valore già salvato nell'istanza
            
auto1 = Auto("AB123CD")
auto2 = Auto("CD123EF")
auto3 = Auto("EF123ZD")

garage1 = Garage(2, [auto1,auto2])

#print(auto1)
#print(garage1)

repeat = True
while repeat:

    print("Auto presenti nel garage:",garage1)
    
    print("1. Parcheggia\n2. Rimuovi\n3. Posti Liberi\n4. Esci")
    option = input("Quale comando vuoi eseguire?\n")                    #Menù per scegliere la funzione da eseguire

    match option:
        case "1":                                                       #caso 1: parcheggia
            targa = input("Targa Auto: ")
            garage1.parcheggia(targa)
        case "2":                                                       #caso 2: rimuovi
            targa = input("Targa Auto: ")
            garage1.rimuovi(targa)
        case "3":                                                       #caso 3: controlla posti liberi
            print("Posti liberi:", garage1.postiliberi())
        case "4":                                                       #caso 4: controllo uscita
            repeat=False                   
        case _:                             
            print ("Comando non valido")



            
                