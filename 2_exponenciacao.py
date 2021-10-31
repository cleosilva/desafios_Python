# Dados números inteiros n e k, com k >= 0, calcular n elevado a k.
n = int(input('Digite um número:'))
k = int(input('Digite o expoente:'))

expo = n ** k
print('O número',n,'elevado ao número',k,'é igual a:',expo)

# Segunda sugestão multiplicando k vezes
# Utilizando laço while
n = int(input('Digite um número:'))
k = int(input('Digite o expoente:'))

pot = 1
i = 0
while i < k:    
    pot = pot * n
    i = i + 1
print('O número',n,'elevado ao número',k,'é igual a:',pot)
