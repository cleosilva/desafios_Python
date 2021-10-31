# Dados um número inteiro n > 0 e as notas finais de n alunos, determinar quantos alunos ficaram de recuperação. 
# Um aluno está de recuperação se sua nota fina está entre 3.0 e 5.0 (exclusive) A nota máxima é 10.0.

alunos = int(input('Digite o número de alunos: '))

contaAlunosRecuperacao = 0
i = 1

while i <= alunos:
    nota = float(input('Digite a nota do aluno: '))
    if nota >= 3 and nota <=5:
        contaAlunosRecuperacao += 1

    i = i + 1

print('Alunos em recuperação: ',contaAlunosRecuperacao)
