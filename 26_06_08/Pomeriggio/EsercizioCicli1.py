#Esercizio 1
#Fare un conto alla rovescia da un numero in input, stampando ogni numero e chiedendo se si vuole ripetere o no
controllore = True

num = int(input("Inserisci un numero: "))
while controllore == True:
    for i in range(num, -1, -1):                                    #start=num, end=-1 (0 incluso), step=-1 (conto alla rovescia)
        print (i)
    scelta = input("Vuoi ripetere il conto alla rovescia?\n")
    if scelta == "no":                                              #check uscita
        controllore = False
    else:
        print("Ripeto il conto alla rovescia:")