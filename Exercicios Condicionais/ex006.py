# Faça um Programa que leia três números e mostre o maior deles.
a = int(input('Insira um número: '))
b = int(input('Insira outro número: '))
c = int(input('Insira o último número: '))

# Estrutura condicional
if a>b and a>c:
    print('O número {} é o maior'.format(a))
elif b>a and b>c:
    print('O número {} é o maior'.format(b))
else:
    print('O número {} é o maior'.format(c))