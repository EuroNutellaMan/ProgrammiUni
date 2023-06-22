#
# Esempio lista random
#
import random #carica una libreria #la libreria random gestisce numeri pseudo-casuali (dipendono da un seed quindi non sono veramente casuali)
#a = numeritabella ** seed /10000 #il seed è quello che determina come il computer trova il numero
#libreria è un insieme di funzioni che posso utilizzare individualmente
#random.random() uso la funzione "random()" della libreria "random"
lista01 = []
lista02 = []
Score = 0

for i in range(100):
    lista01.append(random.randint(1,100)) #aggiungo alla lista un numero int casuale usando la funzione randint della libreria random
    lista02.append(random.randint(1,100))

print("lunghezza: ", len(lista01))

#random.seed() per definire il seed