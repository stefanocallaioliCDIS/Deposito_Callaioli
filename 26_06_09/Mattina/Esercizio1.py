
esercizio = input("Che esercizio vuoi svolgere? ")
match esercizio:
    case "1":
        
        #Esercizio 1
        #Stampa "Pari" se il numero in input è pari e "Dispari" se è dispari

        num = int(input("Inserisci un numero:"))

        if num%2==0:                                                        #check pari/dispari
            print("Pari")
        else:
            print("Dispari")
    
    case "2":
        
        #Esercizio 2
        #Prendi in input un valore intero positivo n e stampa i numeri da n a 0. Rendi il programma ripetibile all'infinito
        
        controllore = True
        while controllore:
            
            num=-1
            while (num<0):
                num = int(input("Inserisci un numero positivo per il conto alla rovescia: "))
            
            for i in range(num, -1, -1):                                    #start=num, end=-1 (0 incluso), step=-1 (conto alla rovescia)
                print (i)
            
            scelta = input("Vuoi ripetere l'esercizio?\n")
            if scelta == "no":                                              #check uscita
                controllore = False
            
    case "3":
        
        #Esercizio 3
        #Prendi in input una lista di numeri e stampa il quadrato di ciascun numero nella lista
        
        maxLista = int(input("Quanti numeri vuoi aggiungere alla lista?"))
        lista = []
        for i in range(maxLista):
            num = int(input("Inserisci un numero nella lista: "))
            lista.append(num)
        for c in lista:
            print (c**2)
        
    case "4":
        #Esercizio 4
        #Prendi in input una lista di interi dall'utente
        
        maxLista = int(input("Quanti numeri vuoi aggiungere alla lista?"))
        lista = []
        for i in range(maxLista):
            num = int(input("Inserisci un numero nella lista: "))
            lista.append(num)

        #Stampa "Lista Vuota" se la lista è vuota, altrimenti trova il numero massimo nella lista e il numero di elementi al suo interno.

        if len(lista)==0:
            print ("Lista Vuota")
        else:
            #Trova numero massimo con un for
            max = lista[0]
            for i in lista:
                if i>max:
                    max=i
            print("Numero massimo: ", max)
                    
            #Conta quanti numeri sono presenti nella lista con un while
            c=0
            while lista:
                lista.pop()
                c+=1
                
            print("Numero di elementi nella lista: ", c)
            
    case _:
        print("Valore non valido")