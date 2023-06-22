#
# Esempio Ciclo while
#
conta=0
numero = input('Digita un numero minore di 10: ')
numero = float(numero)
while numero < 10: #esegue finché la condizione è vera
    print(numero)
    numero = numero *2
    conta = conta +1
print(conta)
#se gli do 0 o un numero negativo non finisce mai