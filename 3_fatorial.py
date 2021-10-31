# Dado um número inteiro n >= 0, calcular n!
# n! = n*(n-1)*(n-2)*...*

n= int(input('Digite o valor de n: '))
fat = 1

i = 2
while i <= n:
    fat = fat * i
    i = i + 1
print('Fatorial de',n,'é:',fat)