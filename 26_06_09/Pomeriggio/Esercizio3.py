#Esercitazione

import random

#Chiede un numero positivo all'utente
def askNumber():
    n = int(input("Inserisci un numero intero positivo: "))
    while (n<0):                                                  
        n = int(input("Numero negativo o uguale a 0. Inseriscine un altro.\n"))
    return n

#Crea una lista di dimensione n contenente int da 1 a n
def createList(n:int):
    list = []
    for i in range(n):
        list.append(random.randint(1, n))
    return list

#Soomma tutti in numeri pari nella lista
def sumEven(list):
    somma = 0
    for i in list:
        if i%2==0:
            somma+=i
    print ("Somma numeri pari nella lista: ",  somma)  

#Stampa tutti i numeri dispari nella lista
def printOdd(list):
    print ("Numeri dispari nella lista:")
    for i in list:
        if i%2==1:
            print(i)
            
#Restituisce True se il numero dato è primo, False altrimenti
def isPrime(num):
    if num==1:
        return False
    else:
        i=2
        while num%i!=0 and i*i<=num:                        #controlliamo solo fino a sqrt(num), dopo sicuramente non sono divisori
            i+=1
        if i*i>num:                                         #controlliamo perché siamo usciti dal while: se siamo arrivati fino a sqrt(num) senza trovare divisori è primo
            return True
        else:
            return False

#Controlla se un numero nella lista è primo, facendo scegliete all'utente
def isPrimeFromList(list):
    index = int(input("Indica l'indice del numero nella lista di cui vuoi controllare la primalità: "))
    num = list[index]
    if isPrime(num):
        print(num, " è primo.")
    else:
        print(num, " non è primo.")

#Stampa i numeri primi nella lista
def printAllPrimes(list):
    for i in list:
        if isPrime(i):
            print(i)

#Controlla se la somma dei numeri nella lista è prima e stampa la risposta
def isSumPrime(list):
    somma = 0
    for i in list:
        somma+=i
    if isPrime(somma):
        print("La somma dei numeri nella lista (",somma,") è prima")
    else:
        print("La somma dei numeri nella lista (",somma,") non è prima")

#Restituisce False se l'utente vuole uscire dall'esercizio, True altrimenti. Necessita di string per il messaggio di input
def checkRepeat(message:str):
    scelta = input(message)
    if scelta == "no":                                             
        return False
    else:
        return True
  

repeat = True
while repeat:

        
    n = askNumber()                                                     #Inizializzazione della lista
    list = createList(n)
    print(list)

    option = input("Quale comando vuoi eseguire?\n")                    #Menù per scegliere la funzione da eseguire
    match option:
        case "1":                           
            sumEven(list)
        case "2":                           
            printOdd(list)
        case "3":                           
            isPrimeFromList(list)
        case "4":                           
            printAllPrimes(list)
        case "5":
            isSumPrime(list)            
        case _:                             
            print ("Comando non valido")

    repeat = checkRepeat("Vuoi eseguire un altro comando?\n")           #Check di uscita


