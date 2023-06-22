#
# Esercizio contatore grandezza valori lista 1 e 2
#
import random
lista01 = []
lista02 = []
Score = 0
conta01 = 0
conta02 = 0
conta03 = 0

for i in range(100):
    lista01.append(random.randint(1,100))
    lista02.append(random.randint(1,100))

print("Lunghezza: ", len(lista01)) #Dice quanto è lunga la lista 1

for i in range(100):
    if lista01[i] > lista02[i]: #se il valore della lista 1 è maggiore
        conta01 = conta01 + 1
    elif lista02[i] > lista01[i]: #se il valore della lista 2 è maggiore
        conta02 = conta02 + 1
    else: #se sono uguali
        conta03 = conta03 + 1

print('I valori della lista 1 sono più grandi ',conta01,' volte')
print('I valori della lista 2 sono più grandi ',conta02,' volte')
print('I valori sono uguali ',conta03,' volte')