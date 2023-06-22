#
# Esercizio ordine crescente 3 numeri
#
a = input('Digita un numero qualsiasi ')
a = float(a)
b = input('Digita un numero qualsiasi ')
b = float(b)
c = input('Digita un numero qualsiasi ')
c = float(c)

if a > b and b > c:
    print(c, b, a)
elif a > b and c > b:
    if a > c:
        print(b, c, a)
    else:
        print(b, a, c)
elif b > a and a > c:
    print(c, a, b)
elif b > a and c > a:
    if b > c:
        print(a, c, b)
    else:
        print(a, b, c)
print('FINITO')