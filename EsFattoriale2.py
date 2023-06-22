# Es fattoriale con while
#
conta=1
numero = input('Digita un numero intero: ')
numero = int(numero)
while numero >= 1:
    conta = conta * numero
    numero = numero -1
print(conta)