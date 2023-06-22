#
# Esempio loop
# Mi conterà tutti i numeri da 0 al numero che metto come input
#
conta=0
ripete = input('Digita un numero intero ')
ripete = int(ripete) #converte in numero intero
for i in range(ripete): #ciclo, funziona solo su liste quindi range crea lista
    print(i) #stesso blocco = stesso rientro, fatto con tab, quando tolgo spazio finisce blocco
    conta = conta +1
print('numero di ripetizioni: ', conta)