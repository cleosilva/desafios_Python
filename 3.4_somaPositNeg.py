# Dados um número inteiro n, n>0, e uma sequência com n números inteiros, 
# determinar a soma dos inteiros positivos e a soma dos inteiros negativos da sequência. 
# Por exemplo, para a sequência  [  6    -2    7   0    -5    8   4 ] o seu programa deve escrever os números 25 e -7.

n = int(input('Digite o tamanho da sequencia: '))
somaPositivos = 0
somaNegativos = 0

i = 1

while i <= n:
    num = int(input('Digite o número da sequência: '))
    if num > 0:
        somaPositivos = somaPositivos + num
    else:
        somaNegativos = somaNegativos + num
    i = i + 1

print('A soma dos númerso positivos é: ',somaPositivos)
print('A soma dos númerso negativos é: ',somaNegativos)
