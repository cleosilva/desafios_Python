# Dados o número n > 0 de alunos de MAC2166 e n notas de uma prova, 
# onde uma nota é um número real entre 0 e 10,calcule a média das notas dos alunos.

n = int(input('Digite o número de alunos: '))

soma = 0
i = 1

while i <= n:
    nota = int(input('Digite a nota: '))
    soma = soma + nota
    i = i + 1

media = soma / n
print("A média das notas é:", media)


