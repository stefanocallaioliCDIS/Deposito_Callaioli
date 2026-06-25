import os

NOME_DEFAULT = "studenti.csv"

def dictToStr(diz):
    stringaFile = "Nome,Voti\n"
    for studente,voti in diz.items():
        for voto in voti:
            stringaFile+=(studente+","+str(voto)+"\n")
    return stringaFile

def strTodict(stringa:str):
    diz={}
    righe=stringa.split("\n")
    righe.pop(0)
    for riga in righe:
        if (riga==""):
            continue
        
        studenteVoto=riga.split(",")
        studente=studenteVoto[0]
        voto=studenteVoto[1]
        
        if studente not in diz:
            diz.setdefault(studente,[])
        diz[studente].append(int(voto))
        
    return diz

def salvaFile(diz,nomeFile=NOME_DEFAULT):
    stringa=dictToStr(diz)
    with open(nomeFile,"w") as file:
        file.write(stringa)    

def caricaFile(nomeFile=NOME_DEFAULT):
    with open(nomeFile,"r") as file:
        contenuto = file.read()
    return strTodict(contenuto)


if not os.path.exists(NOME_DEFAULT):
    with open(NOME_DEFAULT,"w") as file:
        file.write("")
        
diz = caricaFile()

while True:
    
    print("Studenti:")
    id=1
    for nome, voti in diz.items():
        print(f"{id}. {nome} {",".join(map(str, voti))}")
        id+=1
    
    scelta = input("Scegliere un'opzione.\n1) Inserisci studente\n2) Inserisci voto\n3) Visualizza media studenti\n4) Elimina uno studente\n5) Esci")
    match scelta:
        case "1":
            studente = input("Inserire nome nuovo studente: ")
            if studente in diz:
                print("Studente già inserito")
            else:
                diz[studente] = []
                voto = input("Inserire il primo voto: ")
                if voto.isnumeric():
                    voto = int(voto)
                    diz[studente].append(voto)
            salvaFile(diz)
        case "2":
            studente = input("Inserire nome studente: ")
            if studente not in diz:
                print("Studente non presente")
            else:
                voto = input("Inserire voto esame: ")
                if voto.isnumeric():
                    voto = int(voto)
                    diz[studente].append(voto)
                else:
                    print("Formato non valido, inserire un numero")
            salvaFile(diz)
        case "3":
            for nome, voti in diz.items():
                print(f"Nome: {nome}, Media: {round(sum(voti)/len(voti), 2) if len(voti) > 0 else 0}")
        case "4":
            studente = input("Inserire nome studente: ")
            if studente not in diz:
                print("Studente non presente")
            else:
                diz.pop(studente)
                print(studente,"eliminato.")
                salvaFile(diz)
        case "5":
            print("Arrivederci")
            break
        case _:
            print("Comando non valido")
    print("---------------------------------------------------")
