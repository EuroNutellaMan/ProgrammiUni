#
# Trova pattern proteina da file fasta
#
BLUE = '\033[94m'
RESET = '\033[0m'

filein = open(r"UP000000625_83333.fasta", "r") #apre il file #r prima serve solo per sistemi windows #r dopo dice cosa fare (3 opzioni, r = leggi, w = scrivi, altra per modificare)
filelines = filein.readlines() #legge il file una linea alla volta e lo memorizza nella variabile (lista)
filein.close() #chiude il file

conta = 0
proteina = ">"
sequenza = ""
lista_sequenze = []

print(filelines[1]) #(senza [1]) lo scriverà compresso, aprirà una finestra (a capo automatico crasha il mio programma)
#(con [1]) legge solo la 2nda riga

for i in filelines: #trova quante linee hanno la sequenza #i in questo caso è un elemento di filelines
    if proteina in i: #oppure if i == sequenza:
        conta = conta+1

print(BLUE+'Ci sono',conta,'proteine.'+RESET)

for i in filelines: #unisce ogni proteina in un solo elemento
    if proteina in i:
        if sequenza !="": #non aggiunge sequenze vuote
            lista_sequenze.append(sequenza)
        sequenza = ""
        sequenza = sequenza+i.strip('\n') #strip('\n') rimuove quando va a capo
    else:
        sequenza = sequenza+i.strip('\n')
lista_sequenze.append(sequenza) #aggiunge l'ultima sequenza

print('Ci sono', len(lista_sequenze), 'sequenze nella lista')

titolo = ""
lista_titoli = []
seqProt = ""
lista_seqProt = []

for i in filelines: #genera una lista di titoli e una di proteine
    if proteina in i:
        if seqProt != "":
            lista_seqProt.append(seqProt)
        seqProt = ""
        titolo = i.strip('\n')
        lista_titoli.append(titolo)
    else:
        seqProt = seqProt + i.strip('\n')
lista_seqProt.append(seqProt)

print('Ci sono',len(lista_titoli),'titoli.')
print('Ci sono',len(lista_seqProt),'sequenze di proteine.')

AA = input('Quale amminoacido sto cercando? ') #P in questo caso
numAA = 0
lista_numAA = []
seqAA = ""

for i , j in enumerate(lista_seqProt): #conta quante volte una proteina ha l'AA
    seqAA = j
    for k in seqAA:
        if AA == k:
            numAA = numAA+1
    lista_numAA.append(numAA)
    numAA = 0

print(BLUE+'Ho contato AA in',len(lista_numAA),'proteine.')
print('Ci sono un totale di',sum(lista_numAA),AA)
print('In media le proteine hanno',round(sum(lista_numAA)/len(lista_numAA), 2),AA)

magg20 = 0
min20 = 0
none = 0

for i in lista_numAA: #trova quante proteine hanno x AA
    if i >= 20:
        magg20 = magg20+1
    elif i > 0:
        min20 = min20+1
    elif i == 0:
        none = none+1

print(magg20,'proteine hanno almeno 20',AA)
print(min20,'proteine hanno meno di 20',AA)
print(none,'proteine non hanno',AA+RESET)

numProt = input('Quale proteina vuoi trovare (numero intero)? ') #per vedere la sequenza di una specifica proteina
numProt = int(numProt)

print(BLUE,'Titolo: ',lista_titoli[numProt-1].strip('>'))
print('Sequenza: ',lista_seqProt[numProt-1])
print(AA+':',lista_numAA[numProt-1],RESET)