#Esercizio 1
#Login con if annidati

name = input("Inserisci il tuo nome: ")
if name == "Stefano":
    password = input("Inserisci la tua password: ")
    if password == "27037":
        confirm = input("Sicuro di voler accedere? ")
        if confirm == "Confermo":
            print ("Accesso eseguito")
        else:
            print ("Accesso negato")
    else:
        print ("Accesso negato, password sbagliata")
else:
    print ("Accesso negato, nome sbagliato")
