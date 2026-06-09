#Extra lavora su lista invece che su numero


controllore = True
while controllore:
    
    #1.
    #Usa while per garantire che un utente inserisca un numero positivo
    num=-1
    while (num<0):                                                  
        num = int(input("Inserisci un numero intero positivo: "))
        if num<0:
            print("Numero negazivo o uguale a 0. Inseriscine un altro.")
    
    #2.
    #Utilizza un ciclo for con range per calcolare la somma dei numeri pari fra 1 e n
    somma = 0
    for i in range (1,num+1):
        if i%2==0:
            somma+=i
    print ("Somma numeri pari fra 1 e n: ",  somma)   
    
    #3.
    #Utilizza un ciclo for per stampare tutti i numeri dispari da 1 a n
    print ("Numeri dispari fra 1 e n:")
    for i in range (1,num+1):
        if i%2==1:
            print(i)
            
    #4.
    #Utilizza una struttura if per determinare se n è un numero primo
    if num==1:
        print("Non primo")
    else:
        i=2
        while num%i!=0 and i*i<=num:                        #controlliamo solo fino a sqrt(num), dopo sicuramente non sono divisori
            i+=1
        if i*i>num:                                         #controlliamo perché siamo usciti dal while: se siamo arrivati fino a sqrt(num) senza trovare divisori è primo
            print("Primo")
        else:
            print("Non Primo")
        
        #Stiamo facendo molti controlli inutili come su 6 dopo che abbiamo controllato 3 e 2, suoi divisori, sarebbe molto migliorabile con la programmazione dinamica


    scelta = input("Vuoi ripetere l'esercizio?\n")
    if scelta == "no":                                              #check uscita
        controllore = False
