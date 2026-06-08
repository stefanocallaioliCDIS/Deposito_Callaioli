#Esercizio 5
#Calcolatrice che usa match case

num1 = int(input("Inserisci il primo numero: "))
num2 = int(input("Inserisci il secondo numero: "))

operazione = input("Inserisci l'operazione che vuoi svolgere: ")

match operazione:
    case "+":                           #addizione
        print (num1 + num2)
    case "-":                           #sottrazione
        print (num1 - num2)
    case "*":                           #moltiplicazione
        print (num1 * num2)
    case "/":                           #divisione
        if num2 == 0:                   #check divisione per 0
            print ("Errore: Divisione per zero")
        else:
            print (num1 / num2)
    case _:                             #comando non valido
        print ("Operazione non valida")