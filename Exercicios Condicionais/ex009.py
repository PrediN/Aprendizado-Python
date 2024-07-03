# Faça um Programa que leia três números e mostre-os em ordem decrescente.

# Inserção de variavel
a = int(input('Insira o primeiro número: '))
b = int(input('Insira o segundo número: '))
c = int(input('Insira o terceiro número: '))

# Estrutura condicional
if a > b and a > c:
    if b > c:
        print('A ordem decrescente dos números é: {}, {}, {}.'.format(a, b,c))
    else:
        print('A ordem decrescente dos números é: {}, {}, {}.'.format(a, c, b))
elif b > a and b > c:
    if a > c:
        print('A ordem decrescente dos números é: {}, {}, {}.'.format(b, a, c))
    else:
        print('A ordem decrescente dos números é: {}, {}, {}.'.format(b, c, a))
else:
    if a > b:
        print('A ordem decrescente dos números é: {}, {}, {}.'.format(c, a, b))
    else:
        print('A ordem decrescente dos números é: {}, {}, {}.'.format(c, b, a))
