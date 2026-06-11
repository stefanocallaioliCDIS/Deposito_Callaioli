import MODULOLIBRO
import MODULOLIBRERIA

#Creazione libri di esempio
libro1 = MODULOLIBRO.Libro("Il colore della Magia", "Terry Pratchet", "1")
libro2 = MODULOLIBRO.Libro("Lonesome Dove", "Larry McMurtry", "2")
libro3 = MODULOLIBRO.Libro("Lonesome Dove", "Larry McMurtry", "3")

#Esempio creazione libreria e aggiunta libri
libreria1 = MODULOLIBRERIA.Libreria([libro1])
libreria1.aggiungiLibro(libro2)
libreria1.aggiungiLibro(libro3)
libreria1.mostraCatalogo()
print()
'''
Il colore della Magia(1), scritto da Terry Pratchet
Lonesome Dove(2), scritto da Larry McMurtry
Lonesome Dove(3), scritto da Larry McMurtry
'''

#Esempio rimozione libri
libreria1.rimuoviLibro("2")
libreria1.mostraCatalogo()
print()
'''
Il colore della Magia(1), scritto da Terry Pratchet
Lonesome Dove(3), scritto da Larry McMurtry
'''

#Esempio ricerca libri per titolo, aggiunto di nuovo Libro con lo stesso nome
libreria1.aggiungiLibro(libro2)
for libro in libreria1.cercaPerTitolo("Lonesome Dove"):
    print(libro)
'''
Lonesome Dove(3),Larry McMurtry
Lonesome Dove(2),Larry McMurtry
'''