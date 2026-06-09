#Funzioni - blocchi di codice modulari, richiamabili per riutilizzarli in altre parti del programma

#Definizione della funzione
def esempio(parametri):
    #commento sull'uso della funzione
    pass

#Chiamata della funzione
argomenti = "Lorem Ipsum"
esempio(argomenti)

#Esempio di definizione
def saluta(nome):
    print("Ciao,", nome)

#Esempio di funzione definita con 2 parametri
def somma(a,b):
    risultato = a + b
    print("La somma è:", risultato)

#Esempio di chiamate di funzione
saluta("Alice")
somma(5, 3)

#Esempio di tipi di parametri diversi
def saluta(nome:str, messaggio="Ciao"):
    print(f"{messaggio} {nome}!")
    
saluta("Mario")
saluta("Luigi", messaggio="Buongiorno")

#Esempio di funzione con return - il valore nel return viene passato a risultato
def quadrato(numero):
    return numero * numero

risultato = quadrato(4)
print(risultato)