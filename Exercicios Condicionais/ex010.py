# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

# Inserção da variavel
print('='*20)
print('Turno Matutino - M')
print('Turno Vespertino - V')
print('Turno Noturno - N')
print('='*20)
print()
turno = str(input('Insira qual o seu turno: ')).strip().upper()

# Estrutura condicional
if turno == 'M':
    print()
    print('Seu turno é o MATUTINO. Seu horário é das 08:00 às 17:00 com pausa das 12:00 às 13:00')
elif turno == 'V':
    print()
    print('Seu turno é o VESPERTINO. Seu horário é das 16:00 às 01:00 com pausa das 21:00 às 22:00')
    print('Devido ao hórario de saída o fretado espera você no portão da empresa')
elif turno == 'N':
    print()
    print('Seu turno é o NOTURNO. Seu horário é das 00:00 às 09:00 com pausa das 04:00 às 05:00')
    print('O fretado deixará você na porta da empresa e será fornecido café da manhã na saida do turno')
else:
    print('Turno não encontrado favor inserir um turno válido')