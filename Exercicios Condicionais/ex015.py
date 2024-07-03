# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;

print('='*10, 'É UM TRIANGULO?', '='*10)
print()

# Inserção de variaveis
a = int(input('Insira o valor do primeiro lado: '))
b = int(input('Insira o valor do segundo lado: '))
c = int(input('Insira o valor do terceiro lado: '))

# Estrutura condicional para ver se é triangulo
if a+b>c and a+c>b and b+c>a:
    print('É um triangulo!')
    # Estrutura condicional para saber qual o tipo de triangulo ele é
    if a==b==c:
        print('O seu triangulo é um triangulo equilátero!')
    elif a==b or a==c or b==c:
        print('O seu trinagulo é um triangulo Isóceles!')
    elif a!=b!=c:
        print('O seu triangulo é um triangulo escaleno!')
else:
    print('Não é um trinagulo!')

