#Esercizio 2
#semplice crud con if e elif

products = ["Banana", "Mela", "Pera"]

print ("Prodotti attuali: ", products)                              #Stampa dei prodotti
crud = input("Cosa vuoi fare? Create, Read, Update o Delete: ")
if crud == "Create":                                                #Create
    create = input("Prodotto che vuoi aggiungere: ")
    products.append(create)
    print(create, " aggiunto!")
elif crud == "Read":                                                #Read (Già svolto fuori da if, quindi non facciamo nulla)
    pass
elif crud == "Update":                                              #Update (Trovo indice del prodotto e lo uso per sostituirlo)
    update1 = input("Prodotto che vuoi aggiornare: ")
    update2 = input("Nuovo valore del prodotto: ")
    products[products.index(update1)] = update2                 
    print(update1, " modificato!")
elif crud == "Delete":                                              #Delete
    delete = input("Prodotto che vuoi eliminare: ")
    products.remove(delete)
    print(delete, " eliminato!")
else:                                                               #Errore
    print ("Comando non riconosciuto.")
    
print ("Prodotti attuali: ", products)                              #Stampa dei prodotti

    
