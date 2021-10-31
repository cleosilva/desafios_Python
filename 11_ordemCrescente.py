# Dados um número inteiro n, n>0, e uma sequência com n números inteiros, 
# verificar se a sequência está em ordem crescente.

n = int(input('Digite o tamanho da sequência: '))
ant = int(input('Digite o número da sequência: '))

cresce = True
i = 2

while i <= n and cresce:
    num = int(input('Digite o número da sequência: '))
    if num <= ant:
        cresce = False
    ant = num
    i = i + 1
if cresce:
    print('Sequência crescente!')
else:
    print('Sequencia não é crescente!')
