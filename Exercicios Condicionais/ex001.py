# Faça um Programa que peça dois números e imprima o maior deles.
#
# Inserção de variaveis
a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))

# Estrutura condicional
if a>b:
    print('O número {} é maior que {}.'.format(a, b))
else:
    print('O número {} é maior que {}.'.format(b, a))