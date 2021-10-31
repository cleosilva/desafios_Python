# Dados um número inteiro n, n > 0, e uma sequência com n notas finais de MAC2166, determinar quantos alunos:

# estão de recuperação: nota final maior ou igual a 3 e menor do que 5;
# foram reprovados: nota final menor do que 3;
# foram aprovados: nota final maior ou igual a 5;
# tiveram um desempenho muito bom: nota maior que 8; 

alunos = int(input('Digite o número de alunos: '))

contaAlunosReprovados = 0
contaAlunosAprovados = 0
contaAlunosRecuperacao = 0
contaAlunosBomDesempenho = 0

i = 1

while i <= alunos:
    nota = float(input('Digite a nota do aluno: '))
    if nota < 3:
        contaAlunosReprovados += 1
    if nota >= 5:
        contaAlunosAprovados += 1
    if nota >=3 and nota < 5:
        contaAlunosRecuperacao += 1
    if nota > 8:
        contaAlunosBomDesempenho += 1
    i += 1

print('Total de alunos',alunos)
print('Número de alunos reprovados:',contaAlunosReprovados)
print('Número de alunos em recuperação:',contaAlunosRecuperacao)
print('Número de alunos aprovados:',contaAlunosAprovados)
print('Numero de alunos com bom desempenho:',contaAlunosBomDesempenho)



