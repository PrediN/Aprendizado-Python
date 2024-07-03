# Faça um Programa que leia um número e exiba o dia correspondente da semana.
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

# Criação do array
semana = [1, 2, 3, 4, 5, 6, 7]

# Comando do usuário
dia = int(input('Digite um número de 1 até 7: '))

# Estrutura condicional
if dia in semana:
    if dia == 1:
        print('Domingo!')
    elif dia == 2:
        print('Segunda-Feira!')
    elif dia == 3:
        print('Terça-Feira!')
    elif dia == 4:
        print('Quarta-Feira!')
    elif dia == 5:
        print('Quinta-Feira!')
    elif dia == 6:
        print('Sexta-Feira!')
    else:
        print('Sábado!')
else:
    print('Não é um dia da semana!')