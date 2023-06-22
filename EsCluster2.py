# Clustering 2

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

SA = input('inserire simbolo atomo: ')
NA = input('inserire il numero del residuo: ')
SogDist = input('distanza: ')
SogDist = float(SogDist)

for j in CoordATM: #cerco le coordinate degli atomi specificati
    if SA == j[0] and NA == j[2]:
        Coord1 = [j[3], j[4], j[5]]
        print('Atomo:',Coord1)
        check = j[2]

AA_list = []

for j in CoordATM:
    Coord2 = []
    Coord2 = [j[3], j[4], j[5]]
    dist = math.dist(Coord1,Coord2) #calcolo distanza per ogni coordinata
    if dist <= SogDist and j[2] not in AA_list and j[2] != check: #guardo se rientra nel range, non è già nella lista e non è lo stesso AA
        AA_list.append(j[2])

print('Gli amminoacidi nel range sono',len(AA_list),'ovvero: ')
print(AA_list)