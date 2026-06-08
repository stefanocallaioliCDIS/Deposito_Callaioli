#Esercizio 4
#Programma chiede età e rifiuta accesso al film se minorenne

age = int(input("Inserire età: "))
match age:                                                      #match case su età
    case age if age<18:                                         #caso minorenne
        print ("Mi dispiace, non puoi vedere questo film")
    case age if age>=18:                                        #case maggiorenne
        print ("Puoi vedere questo film")
    case _:                                                     #case errore
        print ("ERRORE")    