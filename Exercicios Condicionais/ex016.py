# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
# O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
# Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer
# pedir os demais valores, sendo encerrado;
# Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

from math import sqrt

print('='*10, 'FORMULA DE BHASKARA', '='*10)
print()

# Inserção da variável 'a'
a = float(input('Insira o valor de A: '))

if a != 0:
    # Inserção das variáveis 'b' e 'c'
    b = float(input('Insira o valor de B: '))
    c = float(input('Insira o valor de C: '))

    # Calculo do delta
    delta = (b**2) - (4*a*c)

    # Estrutura condicional
    if delta < 0:
        print('A equação não tem raízes reais.')
    elif delta == 0:
        x = -b / (2*a)
        print('A equação possui apenas uma raiz real: x = {:.2f}'.format(x))
    else:
        x1 = (-b + sqrt(delta)) / (2*a)
        x2 = (-b - sqrt(delta)) / (2*a)
        print('A equação possui duas raízes reais: x1 = {:.2f} | x2 = {:.2f}'.format(x1, x2))
else:
    print('A equação não é de segundo grau.')