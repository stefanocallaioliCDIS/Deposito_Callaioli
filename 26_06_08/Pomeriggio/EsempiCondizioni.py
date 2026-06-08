#Condizioni

#If - Esegue il codice al suo interno se la condizione è True

numero = 10
if numero == 10:                    #True
    print ("Vengo eseguito")
if numero != 10:                    #False
    print ("Non vengo eseguito")

#Output: "Vengo eseguito"


#Else - Esegue il codice al suo interno se la condizione nell'if risulta False

if numero == 9:                    #False
    print ("Vengo eseguito io")
else:
    print ("Oppure io")
#Output: "Oppure io"    


#Elif - Esegue il codice al suo interno se le condizioni negli if/elif precedenti risultano False

if numero == 9:                    #False
    print ("Vengo eseguito io")
elif numero == 11:                 #False
    print ("Oppure io")
else:
    print ("Altrimenti io")
#Output: "Altrimenti io"



#match - case - Esegue il codice all'interno del case che ha lo stesso valore della variabile data in input, le condizioni sono controllate sequenzialmente
# case _ è il caso di default
comando = input("Inserisci un comando: ")

match comando:
    case "start":
        print("Avvio dal proframma.")
    case "stop":
        print("Chiusura del programma.")
    case "pausa":
        print("Programma in pausa.")
    case _:
        print("Comando non riconosciuto.")
                