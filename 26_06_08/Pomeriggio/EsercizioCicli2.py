#Esercizio 2
#Chiedere di inserire un numero. Se è pari salvalo. Ferma il programma quando si raggiungono 5 numeri pari.

controllore = True
pari = []                                       #Dichiariamo una lista vuota per salvare i numeri pari

while controllore == True:
    
    num = int(input("Inserisci un numero: "))
    if num%2==0:                                #Check numero pari
        pari.append(num)
        print ("Il numero è pari.")
    else:
        print("Il numero non è pari.")
    
    if len(pari) == 5:                          #Check quantità di numeri pari finora
        controllore = False
print ("I numeri pari sono ", pari)