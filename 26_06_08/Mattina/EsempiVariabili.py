#print - Funzione incorporata per stampare output
name = "Stefano"
age = 27
print("Il mio nome è", name, "e ho", age, "anni.")


"""
#input Funzione incorporata per accettare input dall'utente
name = input("Inserisci il tuo nome: ")
age = int( input("Inserisci la tua età: "))
print("Il mio nome è", name, "e ho", age, "anni.")
"""

#Operazioni aritmentiche
print(1+2)      #somma
print(10-5)     #sottrazione
print(3*2)      #moltiplicazione
print(8/2)      #divisione
print(3**2)     #elevamento a potenza

#Esempi variabili

#int (Interi)
x = 10
y = -10

#float (Numeri in virgola mobile)
a = 3.6
b = - 9.1

#str (stringhe/sequenza di caratteri) 
msg = "Test"
print(name + " " + msg)                                     #Concatenazione -> "Stefano Test"
print(name[0])                                              #'S'
print(name[3])                                              #'f'

print(len(name))                                            #Lunghezza stringa -> 7
print(name.upper())                                         #Rendi maiuscolo -> "STEFANO"
print(name.lower())                                         #Rendi minuscolo -> "stefano"
print((name + " " + msg).replace("Stefano","Marco"))        #Sostituisci nella stringa -> "Marco Test"

#bool (Boolean)
vero = True
falso = False
print (vero)
print (falso)

#Operatori di confronto
'''
==      uguale
!=      diverso
<       minore
>       maggiore
<=      minore e uguale
>=      maggiore e uguale
'''

x = 5
y = 10
print(x == y)   #False
print(x != y)   #True
print(x < y)    #True

#Operatori logici
'''
and     AND logico
1   1   |   1
1   0   |   0
0   1   |   0
0   0   |   0

or      OR logico
1   1   |   1
1   0   |   1
0   1   |   1
0   0   |   0

not     NOT logico
1   |   0
0   |   1

Ordine precedenza: NOT > AND > OR
'''

x=5
y=10
z=7
print (x < y and y > z)     #True
print(x < y or z > y)       #False
print(not(x < y))           #False

#Liste (Collezioni eterogenee, ordinate, modificabili)
numeri = [1, 2, 3, 4, 5]
names = ["Alice", "Bob", "Charlie"]
misto = [1, "due", True, 4.5]

print(misto[2])             #True
print(names[0])             #Alice

print(len(numeri))
numeri.append(6)            #Inserisci valore in fondo a lista
print(numeri)               #[1, 2, 3, 4, 5, 6]
numeri.insert(2, 10)        #Inserisci 10 in posizione 2
print(numeri)               #[1, 2, 10, 3, 4, 5, 6]
numeri.remove(4)            #Rimuovi valore in posizione 4
print(numeri)               #[1, 2, 10, 3, 5, 6]
numeri.sort()               #Ordina i valori nella lista
print(numeri)               #[1, 2, 3, 5, 6, 10]
