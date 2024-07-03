# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

# Inserção de varivel
num = int(input('Insira um número qualquer: '))

# Estrutura condicional
if num >=0:
    print('{} é um número positivo!'.format(num))
else:
    print('{} é um número negativo!'.format(num))