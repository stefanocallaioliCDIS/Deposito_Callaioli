#Modulo Libro
class Libro:
    def __init__(self, titolo:str, autore:str, isbn:str):
        self.titolo = titolo
        self.autore = autore
        self.isbn = isbn
        
    def __str__(self):
        return (self.titolo +  "(" +  self.isbn + ")," + self.autore)
        
    def descrizione(self):
        return (self.titolo +  "(" +  self.isbn + "), scritto da " + self.autore)