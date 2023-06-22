#
# Esempio if
#
numinp = input("inserire un numero qualsiasi ")
numinp = float(numinp)

if numinp > 10: #se è vera fa questo
    numinp = numinp - 1
    print(numinp**2)
elif numinp > 0: #seconda condizione se non è vera quella if
    print(numinp**0.5)
else: #se tutte le altre non sono vere fa questo (senza condizioni)
    print(numinp * 2 + 80)
print('finito') #lo fa sempre