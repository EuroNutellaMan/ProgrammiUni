# clustering di dati metabolomici

import math

filein = open(r"12ca.pdb", "r")
filelines = filein.readlines()
filein.close()

CoordATM = []

for i in filelines:
    a = i.split() #split divide la riga in una lista di elementi
    if a[0] == 'ATOM' or a[0] == 'HETATM': #se il primo elemento è ATOM o HETATM
        #b = a[2]+a[3]+a[5] #Identifica tipo di atomo e di quale AA #non lo uso perché devo controllare spaziatura utente quando cerca
        x = float(a[6]) #trasformo coordinate del file da str a float
        y = float(a[7])
        z = float(a[8])
        CoordATM.append([a[2],a[3],a[5],x,y,z]) #aggiungo le coord alla lista

SA1 = input('inserire simbolo atomo 1: ')
NA1 = input('inserire il numero del residuo 1: ')

SA2 = input('inserire simbolo atomo 2: ')
NA2 = input('inserire il numero del residuo 2: ')

for j in CoordATM: #cerco le coordinate degli atomi specificati
    if SA1 == j[0] and NA1 == j[2]:
        Coord1 = [j[3], j[4], j[5]]
        print('Atomo 1:',Coord1)
    elif SA2 == j[0] and NA2 == j[2]:
        Coord2 = [j[3], j[4], j[5]]
        print('Atomo 2:',Coord2)

dist = math.dist(Coord1, Coord2) #calcolo distanza tra le due coordinate
print('Distanza:',dist,'A')