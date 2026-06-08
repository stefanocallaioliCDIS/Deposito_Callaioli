#while - ripete il codice al suo interno finché la condizione data è True

conteggio = 0
while conteggio < 5:
    print(conteggio)
    conteggio += 1

'''
Output:
0
1
2
3
4
'''


#Ciclo aritmetico - numero di iterazioni deterministico
conteggio = 0
while conteggio < 5:
    print(conteggio)
    conteggio += 1

#vs.

#Ciclo booleano - numero di iterazioni indeterminato
controllore = True
while controllore:
    scelta = input("Vuoi continuare?\n")
    if scelta == "no":
        controllore = False
        
        
#for - ripete il codice al suo interno iterando su un oggetto iterabile (come una lista o una tupla)

numeri = [1,2,3,4,5]
for numero in numeri:
    print(numero)
'''
Output:
1
2
3
4
5
'''
    
#range() - restituisce una sequenza di numeri in base ai parametri passati:
#range([start=0], stop, [step=1])

for i in range(5):
    print(i)

'''
Output:
0
1
2
3
4
'''

for i in range(2,8):
    print(i)
    
'''
Output:   
2
3
4
5
6
7
'''

for i in range(1, 10, 2):
    print(i)

'''
Output:    
1
3
5
7
9
'''