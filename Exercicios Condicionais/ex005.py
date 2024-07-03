# Faça um programa para a leitura de duas notas parciais de um aluno.
# O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

# Inserção de variaveis
nota1 = float(input('Insira sua primeira nota: '))
nota2 = float(input('Insira sua segunda nota: '))

# Calculos da nota
media = (nota1+nota2)/2

# Estrtura condiconal
if media == 10:
    print('Parabéns Aprovado com 10 de média!')
elif media >= 7:
    print('Parabéns aprovado!')
else:
    print('Você foi reprovado!')