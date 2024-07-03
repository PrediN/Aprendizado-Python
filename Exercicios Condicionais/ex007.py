# Faça um Programa que leia três números e mostre o maior e o menor deles.

# Inserção de variaveis
a = int(input('Insira o primero número: '))
b = int(input('Insira o segundo número: '))
c = int(input('Insira o terceiro número: '))

# Estrutura condicional
if a < b and a < c:
    print('O menor número é {}.'.format(a))
elif b<a and b<c:
    print('O menor número é {}.'.format(b))
else:
    print('O menor número é {}.'.format(c))