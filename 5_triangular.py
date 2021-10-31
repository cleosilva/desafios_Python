# Dizemos que um número inteiro positivo é triangular se ele é o produto de três números inteiros consecutivos. 
# Por exemplo, 120 é triangular, pois 4*5*6 é igual a 120. 
# Dado um número inteiro positivo n, verificar se n é triangular.

n = int(input('Digite o valor de n: '))

i = 1 # porque se for zero a multiplicação dará sempre zero
while i*(i+1)*(i+2) < n:
    i = i + 1

if i*(i+1)*(i+2) == n:
    print('É triangular, ',i,'*',i+1, '*', i+2,'=',n,sep=' ')
else:
    print('Não é triangular!')
