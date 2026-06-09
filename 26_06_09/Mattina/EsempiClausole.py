#pass - Non fa niente quando eseguito, usato come placeholder per stutturare il codice evitando errori di sintassi
print("pass:")
for i in range(5):
    if i == 3:
        pass
    print(i)
    
#continue - Salta direttamente all'iterazione successiva di un ciclo quando eseguito
print("continue:")
for i in range(5):
    if i == 3:
        continue
    print(i)
    
#break - Esce direttamente dal ciclo quando eseguito
print("break:")
for i in range(5):
    if i == 3:
        break
    print(i)
    
#Esempio con tutte le clausole
print("Tutti:")
for i in range(5):
    if i == 1:
        pass
    if i == 2:
        continue
    if i == 4:
        break
    print(i)
    

#Operatore * (splat) - trasforma iterabili in una collezione (es. in [] diventa una lista)
print("splat")
numeri = [*range(1, 11)]
print(numeri)