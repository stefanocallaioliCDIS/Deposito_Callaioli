#Tuple - liste immutabili - dimensione scelta e fissata alla valorizzazione
#tuple()
#Eterogeneo
#Ordinata
#Non modificabile
#Accetta duplicati

#Esempi tuple
punto = (3,4)
colore_rgb = (255, 128, 0)
informazioni_persona = ("Alice", 25, "Femmina")

#Esempio senza ()
punto = 3,4
x, y = punto
print(x, y)
'''
3 4
'''


#Accesso a tupla
punto = (3,4)
print(punto[0])
print(punto[1])
'''
3
4
'''


#Set - Insiemi, struttura dati non ordinata
#Eterogeneo (Ma non ha molto senso usarlo in questo modo)
#Non ordinato
#Modificabile
#Non accetta duplicati

#Esempio set
set1 = set([1, 2, 3, 4, 5])
set2 = {4, 5, 6, 7, 8}

set3 = {1, 2, 3, 3, 4, 4, 5}
print(set3)
'''
{1, 2, 3, 4, 5}
'''

#operazioni sugli insiemi
#union() - |                Unione di 2 insiemi
#intersection() - &         Valori in comune dei 2 insiemi
#difference() - -           Valori non in comune con il secondo insieme del primo insieme
#symmetric_difference - ^   Valori non in comune dei 2 insiemi

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.union(set2))                 # Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(set1.intersection(set2))          # Output: {4, 5}
print(set1.difference(set2))            # Output: {1, 2, 3}
print(set1.symmetric_difference(set2))  # Output: {1, 2, 3, 6, 7, 8}

'''
add()
remove()
discard()
len()
in
copy()
'''

#Dizionario - 

studente = {
    "nome": "Alice",
    "eta": 20,
    "sesso": "Femmina"
}

print(studente["nome"]) #output: Alice
print(studente["eta"])  #output: 21

#Esempio modifica e aggiunta chiave
studente["eta"]=21
studente["citta"]="Roma"

print(studente)
#{'nome': 'Alice', 'eta': 21, 'sesso': 'Femmina', 'citta': 'Roma'}

print(studente.keys())      #dict_keys(['nome', 'eta', 'sesso', 'citta'])
print(studente.values())    #dict_values(['Alice', 21, 'Femmina', 'Roma'])
print(studente.items())     #dict_items([('nome', 'Alice'), ('eta', 21), ('sesso', 'Femmina'), ('citta', 'Roma')])

#Ciclare un dizionario
for x,y in studente.items():
    print(x,y)
    
for key in studente.keys():
    print(key, studente[key])


