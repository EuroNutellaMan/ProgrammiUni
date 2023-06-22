#
# Trova pattern in una lista
#
lista = ['qwe', 'atyr', 'tyq', 'cde01']
patt = input('Quale pattern devo trovare? ')

for i in range(len(lista)): #posso anche semplicemente fare "in lista"
    print(lista[i])
    if patt in lista[i]: #se faccio "in lista" uso "i" invece di "lista[i]"
        print('Trovato!')
    else:
        print('Non trovato!')