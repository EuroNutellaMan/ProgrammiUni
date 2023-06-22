#
# Esempio calcolo media e somma
#
#lista[]
#lista.append(56) #aggiunge elementi in fondo
#len(lista) #dice quanti elementi sono sulla lista
#lista.pop(1) elimina il secondo elemento
#lista=[] svuota la lista
lista = []
somma=0
n_val = input('Quanti valori volete valutare? ')
n_val = int(n_val)
while len(lista) < n_val:
    a = input('Digita un numero: ')
    a = float(a)
    lista.append(a)
for i in range(n_val):
    numero = lista[i]
    numero = float(numero)
    somma = somma + numero
print('Somma: ', somma)
print('Media: ', somma/n_val)