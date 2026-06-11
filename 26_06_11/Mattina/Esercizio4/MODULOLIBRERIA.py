#Modulo Libreria

import MODULOLIBRO

class Libreria:
    def __init__(self, catalogo):
        self.catalogo = catalogo
    
    #Metodo che stampa il catalogo
    def mostraCatalogo(self):
        for libro in self.catalogo:
            print(libro.descrizione())    
    
    #Metodo che aggiunge un libro al catalogo 
    def aggiungiLibro(self,libro:MODULOLIBRO.Libro):
        self.catalogo.append(libro)
    
    #Metodo che rimuove un libro dal catalogo (usando isbn)
    def rimuoviLibro(self, isbn:str):
        for libro in self.catalogo:
            if libro.isbn==isbn:
                self.catalogo.remove(libro)
                return                              #possiamo assumere che l'isbn sia univoco, quindi possiamo uscire
    
    #Metodo che restituisce una lista con tutti i libri con lo stesso titolo
    def cercaPerTitolo(self, titolo:str):
        libriTrovati = []
        for libro in self.catalogo:
            if libro.titolo == titolo:
                libriTrovati.append(libro)
        return libriTrovati