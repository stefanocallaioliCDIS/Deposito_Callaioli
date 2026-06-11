#Modulo - file che contiene definizioni di variabili, funzioni e classi usabili da altri file Python
#Si può importare un modulo utilizzando import <nome del file>

import MioModulo

MioModulo.saluta("Alice")                   #Stampa "Ciao, Alice"

raggio = 2
cerchio = MioModulo.Cerchio(raggio)
print(cerchio.area())                       #Stampa l'area del cerchio con raggio 2