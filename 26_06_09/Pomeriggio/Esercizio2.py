#Esercizio 2 - Stampa la sequenza di Fibonacci fino al numero più grande minore di num (dato in input dall'utente)

def fibonacci(num:int):
    x=0
    y=1
    
    while x<=num:
        print (x)
        temp= x+y
        x = y
        y = temp

#Chiede un numero intero positivo all'utente
def askNumber():
    num = int(input("Inserisci un numero: "))
    return num

#Restituisce False se l'utente vuole uscire dall'esercizio, True altrimenti. Necessita di string per il messaggio di input
def checkRepeat(message:str):
    scelta = input(message)
    if scelta == "no":                                             
        return False
    else:
        return True
    

        
        
        
repeat = True
while repeat:
    
    num = askNumber()
    
    fibonacci(num)
    
    repeat = checkRepeat("Vuoi ripetere l'esercizio? ")
