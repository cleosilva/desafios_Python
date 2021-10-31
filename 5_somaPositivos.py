# Dados um número inteiro n, n>0, e uma sequência com n números inteiros, 
# determinar a soma dos inteiros positivos da sequência. 
# Por exemplo, para a sequência  [6    -2    7   0    -5    8   4] o seu programa deve escrever o número 25.

n = int(input('Digite o tamanho da sequencia: '))

soma = 0
i = 1 # inicia a sequencia na base 1

while i <= n:
    num = int(input('Digite o número da sequencia: '))
    if num > 0:
        soma = soma + num
    i = i + 1

print('A soma dos números positivos é:', soma)


