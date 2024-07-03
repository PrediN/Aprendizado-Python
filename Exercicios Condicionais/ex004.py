# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = str(input('Insira uma letra: ')).strip().lower()
vogal = ['a', 'e', 'i', 'o', 'u']

if letra in vogal:
    print('A sua letra escolhida é uma vogal!')
else:
    print('A sua letra escolhida é uma consoante!')
