# Escreva um programa que determina a data cronologicamente maior entre duas datas fornecidas pelo usuário. 
# Cada data deve ser fornecida por três valores inteiros onde o primeiro representa um dia, o segundo um mês 
# e o terceiro um ano.

# Primeira data
print('-------- Entre com a primeira data --------')
d1 = int(input('Dia: '))
m1 = int(input('Mês: '))
a1 = int(input('Ano: '))

# Segunda data
print('\n--------- Entre com a segunda data ---------')
d2 = int(input('Dia: '))
m2 = int(input('Mês: '))
a2 = int(input('Ano: '))

if a1 > a2 or (a1 == a2 and m1 > m2) or (a1 == a2 and m1 == m2 and d1 > d2):
    print('Data 1 é maior!')
elif a1 == a2 and m1 == m2 and d1 == d2:
    print('As datas são iguais!')
else:
    print('Data 2 é maior!')


