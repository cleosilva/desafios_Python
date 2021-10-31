# Dados um número inteiro n, n > 0, e uma sequência com n números inteiros, 
# determinar quantos números da sequência são pares e quantos são ímpares.
numSequencia = int(input('Digite o tamanho da sequencia:'))
contaPares = 0
contaImpares = 0

i = 1 #  inicia a sequência com base 1
while i <= numSequencia:
    num = int(input('Digite um número da sequencia:'))
    if num % 2 == 0:
        contaPares = contaPares + 1
    else:
        contaImpares = contaImpares + 1
    i = i + 1

print(contaPares,'números pares')
print(contaImpares,'números ímpares')


