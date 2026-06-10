'''
Sistema bancario con diverse operazioni:
- stampare informazioni di tutti gli utenti
- registrare utente
- eliminare utente
- deposito
- prelievo
- trasferimento di denaro da un utente ad un altro
- (extra) decoratore per implementare logging dei movimenti bancari 

Non ho fatto in tempo a implementare l'extra
'''

#Restituisce False se l'utente vuole uscire, True altrimenti. Necessita di string per il messaggio di input
def checkRepeat(message:str):
    scelta = input(message)
    if scelta == "no":                                             
        return False
    else:
        return True

#Generatore che ritorna gli utenti uno alla volta
def generatoreUtenti(utenti):
    for index in range(len(utenti)):                                            #Range è poco utile qui, ma è stato inserito per completezza.
        yield utenti[index]                                          
        
#Stampa tutti gli utenti a schermo con il loro bilancio        
def stampaUtenti(utenti):
    i=0
    for nome, bilancio in generatoreUtenti(utenti):
        print(i,"-",nome, ": ", bilancio, "€" )
        i+=1

#Crea un utente, con check per assicurarsi che l'importo sia valido
def creaUtente(utenti):
    nomeUtente = input("Inserisci il nome del cliente: ")
    deposito = int(input("Inserisci il valore del deposito iniziale: "))
    while (deposito<0):                                                  
        deposito = int(input("ERRORE: Deposito negativo. \nInserisci il valore del deposito iniziale: "))
    utente = [nomeUtente, deposito]
    utenti.append(utente)
    print("Creato account per ", nomeUtente, ".")
    return utenti

#Elimina un utente dato il suo indice
def eliminaUtente(utenti):
    stampaUtenti(utenti)
    index = int(input("Indica l'indice dell'utente che vuoi eliminare: "))
    utente = utenti.pop(index)
    print("Eliminato account di ", utente[0], ".")
    return utenti

#Preleva dall'account di un utente, dato il suo indice
def prelievo(utenti):
    stampaUtenti(utenti)
    index = int(input("Indica l'indice dell'utente che vuole prelevare: "))
    importo = int(input("Indica l'importo del prelievo: "))
    while (importo>utenti[index][1] or importo<0):                                                  
        importo = int(input("ERRORE: Importo troppo grande o minore di 0. \nIndica l'importo del prelievo: "))
    utenti[index][1]-=importo
    print("Prelievo avvenuto con successo. \n Bilancio attuale: ", utenti[index][1], "€" )
    return utenti

#Deposita sull'account di un utente, dato il suo indice
def deposito(utenti):
    stampaUtenti(utenti)
    index = int(input("Indica l'indice dell'utente che vuole depositare: "))
    importo = int(input("Indica l'importo del deposito: "))
    while (importo<0):                                                  
        importo = int(input("ERRORE: Importo minore di 0. \nIndica l'importo del deposito: "))
    utenti[index][1]+=importo
    print("Deposito avvenuto con successo. \n Bilancio attuale: ", utenti[index][1], "€" )
    return utenti

#Trasferisce denaro fra due utenti, dato il loro indice
#Sarebbe migliorabile rendendo deposito() e prelievo() più generiche, evitando ripetizioni
def trasferimento(utenti):
    stampaUtenti(utenti)
    index1 = int(input("Indica l'indice dell'utente che vuole traferire ad un altro utente: "))
    index2 = int(input("Indica l'indice dell'utente che deve ricevere il denaro: "))
    importo = int(input("Indica l'importo del trasferimento: "))
    while (importo>utenti[index1][1] or importo<0):                                                                         
        importo = int(input("ERRORE: Importo troppo grande o minore di 0. \nIndica l'importo del prelievo: "))
    utenti[index1][1]-=importo
    utenti[index2][1]+=importo
    print("Trasferimento avvenuto con successo. \n Bilancio attuale:\n", utenti[index1][0], ": ", utenti[index1][1], "€\n", utenti[index2][0], ": ", utenti[index2][1], "€\n")
    return utenti


utenteTest1 = ["Nicola Bianchi", 50]
utenteTest2 = ["Luisa Neri", 130]
utenteTest3 = ["Sofia Rossi", 75]
utenteTest4 = ["Marco Verdi", 100]

utenti = [utenteTest1, utenteTest2, utenteTest3, utenteTest4]
#Lista di Utenti, definiti da Nome (Indice 0) e Bilancio (Indice 1)



repeat = True
while repeat:

    print("1. Mostra tutti i clienti della banca\n2. Registra un nuovo utente\n3. Elimina un utente\n4. Prelievo\n5. Deposito\n6. Trasferimento")
    option = input("Quale comando vuoi eseguire?\n")                    #Menù per scegliere la funzione da eseguire

    match option:
        case "1":                           
            stampaUtenti(utenti)
        case "2":                           
            utenti = creaUtente(utenti)
        case "3":                           
            utenti = eliminaUtente(utenti)
        case "4":                           
            utenti = prelievo(utenti)
        case "5":
            utenti = deposito(utenti)
        case "6":
            utenti = trasferimento(utenti)          
        case _:                             
            print ("Comando non valido")

    repeat = checkRepeat("Vuoi eseguire un altro comando?\n")           #Check di uscita