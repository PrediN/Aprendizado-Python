# Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

# Inserção de variavel
sexo = str(input('Insira a primeira letra do seu sexo: ')).strip().capitalize()

# Estrutura condicional
if sexo == 'F':
    print('Sexo Feminino')
elif sexo == 'M':
    print('Sexo Masculino')
else:
    print('Sexo Inválido')