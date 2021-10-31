# Dados um número inteiro n, n > 0, e um dígito d. 0 <= d <= 9, determinar quantas vezes d ocorre em n.

n = int(input('Digite o valor de n:'))
d = int(input('Digite o valor de d [0 a 9]:'))

num = n
cont = 0

while n != 0:
    resto = n % 10
    if resto == d:
        cont = cont + 1
    n = n // 10 # Novo valor de n
print(d,'ocorre',cont,'vezes em', num)


