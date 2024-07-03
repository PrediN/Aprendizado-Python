# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina
# ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

# Média de Aproveitamento  Conceito
# Entre 9.0 e 10.0        A
# Entre 7.5 e 9.0         B
# Entre 6.0 e 7.5         C
# Entre 4.0 e 6.0         D
# Entre 4.0 e zero        E

# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente
# e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

# Inserção de variaveis
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

# Calculo da media
media = (nota1+nota2)/2
print()

if media >= 9:
    print('Sua nota final foi {}, sua média do boletim é: "A"!'.format(media))
    print('APROVADO')
elif media >= 7.5 and media < 9:
    print('Sua nota final foi {}, sua média do boletim é: "B"!'.format(media))
    print('APROVADO')
elif media >= 6 and media < 7.5:
    print('Sua nota final foi {}, sua média do boletim é: "C"!'.format(media))
    print('APROVADO')
elif media >= 4 and media < 6:
    print('Sua nota final foi {}, sua média do boletim é: "D"!'.format(media))
    print('REPROVADO')
else:
    print('Sua nota final foi {}, sua média do boletim é: "E"!'.format(media))
    print('REPROVADO')