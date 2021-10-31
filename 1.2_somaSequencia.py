# Dada uma sequência de números inteiros diferentes de zero, terminada por um zero, calcular a sua soma.
print('Digite uma sequencia de números e tenha a sua soma total, digite zero para sair')

num = int(input('Digite um número:')) # primeiro número

soma = 0
while num != 0:
    soma = soma + num
    num = int(input('Digite um número:')) # demais númerso até sair com zero

print("A soma é:",soma)

