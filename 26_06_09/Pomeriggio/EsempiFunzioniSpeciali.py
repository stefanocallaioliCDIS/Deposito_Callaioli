#yield -    Usabile per creare una funzione generatore, ovvero una funzione "iterarabile". 
#           Mentre il return interrompe l'esecuzione della funzione, yield la sospende e rende possibile tornare a eseguire la funzione dallo stato in cui l'avevamo lasciata

def fibonacci(n):
    a = 0
    b = 1
    
    while a < n:
        yield a 
        a = b
        b = a + b
print(list(fibonacci(10)))        
print([*fibonacci(10)])

for numero in fibonacci(10):
    print(numero)

    
# @ - decoratore 
# Permette di ricevere una funzione come input. Contiene un wrapper definito al suo interno, che può modificare la funzione originale prima o dopo 
def decoratore(funzione):
    def wrapper():
        print("Prima dell'esecuzione della funzione")
        funzione()
        print("Dopo l'esecuzione della funzione")
    return wrapper

@decoratore             
def saluta():
    print("Ciao")
    
saluta()

'''
Output:
Prima dell'esecuzione della funzione
Ciao
Dopo l'esecuzione della funzione
'''

#E' possibile usare più di un decoratore sulla stessa funzione
@decoratore 
@decoratore             
def saluta():
    print("Ciao")
    
'''
Output:
Prima dell'esecuzione della funzione
Prima dell'esecuzione della funzione
Ciao
Dopo l'esecuzione della funzione
Dopo l'esecuzione della funzione
'''

#*args, **kwargs assicurano che il wrapper possa accettare tutti  gli argomenti passati nella funzione originale

def decoratore_con_argomenti(funzione):
    def wrapper(*args, **kwargs):
        print("Prima")
        risultato = funzione(*args, **kwargs)
        print("Dopo")
        return risultato
    return wrapper

@decoratore_con_argomenti
def somma(a,b):
    print(a+b)
    return a+b

print("risultato è", somma(3,4))

'''
Prima
7
Dopo
risultato è 7
'''

#Esempio: usare un decoratore per calcolare il tempo di esecuzione di una funzione calcolo_lento
import time

def calcola_tempo(funzione):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        risultato = funzione(*args,**kwargs)
        end_time=time.time()
        print(f"Tempo di esecuzione:{end_time - start_time}")
        return risultato
    return wrapper

@calcola_tempo
def calcolo_lento():
    time.sleep(2)
    print("Calcolo completato")
    
#Chiamata alla funzione decorata
calcolo_lento()

'''
Output:
Calcolo completato
Tempo di esecuzione:2.0006139278411865
'''