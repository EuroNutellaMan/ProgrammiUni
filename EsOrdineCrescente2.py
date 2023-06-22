#
# Esempio Ordine Crescente 2
#
a = input('Digita un numero qualsiasi ')
a = float(a)
b = input('Digita un numero qualsiasi ')
b = float(b)
c = input('Digita un numero qualsiasi ')
c = float(c)

if a > b:
    a, b = b, a # scambio i numeri dove in a ho il minore fra a e b

if a > c:
    a, b, c = c, a, b #c è il più piccolo dei tre
elif b > c:
    b, c = c, b # c è maggiore di a ma minore di b

print(a, b, c)