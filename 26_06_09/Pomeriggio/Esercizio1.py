#Esercizio 1
#Crea un gioco usando le funzioni. L'utente deve provare a indovinare un numero casuale fra 1 e 100. Se si sbaglia viene dato un suggerimento.

import random

#Chiede un numero intero positivo all'utente
def askNumber():
    num = int(input("Inserisci un numero intero: "))
    return num

#Restituisce False se l'utente vuole uscire dall'esercizio, True altrimenti. Necessita di string per il messaggio di input
def checkRepeat(message:str):
    scelta = input(message)
    if scelta == "no":                                             
        return False
    else:
        return True

#Funzione principale, il giocatore vince quando indovina il valore passato in input
def gioca (goal:int):
    print("Indovina un numero fra 1 e 100")
    continua = True
    while continua:
        num = askNumber()
        if num == goal:
            print("Hai vinto!")
            break
        elif num<goal:
            print("Il numero è più piccolo")
        else:
            print("Il numero è più grande")
        continua = checkRepeat("Vuoi continuare a provare a indovinare? ")


repeat = True
while repeat:
    
    num = random.randint(1, 100)
    print(num)
    
    gioca(num)
    
    repeat = checkRepeat("Vuoi ripetere l'esercizio? ")
