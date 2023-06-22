#
# Calcolo fattoriale di un numero
#
fattoriale=1
ripete = input('Digita un numero intero: ')
ripete = int(ripete)
for i in range(ripete):
    print(i+1)
    fattoriale = fattoriale * (i+1) #i va da 0 a 3 se inserisco 4, quindi devo fare +1 perché lui conta da 0
print('Risultato: ', fattoriale)
#se range è 0 o negativo salta la parte con for e mi da 1