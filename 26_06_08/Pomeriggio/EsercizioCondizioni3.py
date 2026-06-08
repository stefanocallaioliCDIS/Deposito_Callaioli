#Esercizio 3
#semplice Registrazione o Login con if - elif - else

loginName= "admin"
loginPassword = "password"
id = 142

options = input("Registrazione o Login: ")
if options == "Registrazione":
    name = input("Inserisci nome: ")
    password = input("Inserisci password: ")
    id+=1
    
    print ("Account ", id, "creato: ", name)
elif options == "Login":
    name = input("Inserisci nome: ")
    password = input("Inserisci password: ")
    if (name == loginName and password == loginPassword):
        print ("Accesso eseguito.")
    else:
        print ("Accesso negato.")
else:
    print ("Comando non riconosciuto.")