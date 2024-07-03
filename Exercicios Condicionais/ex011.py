# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

print('='*10, 'CALCULADORA DE AUMENTO', '='*10)

# Inserção de variavel
salario = int(input('Insira o seu valor de salário: R$'))

if salario > 0 and salario <= 280:
    aumento = salario*0.2
    print('Seu salário antes do reajuste era de: R${:.2f}'.format(salario))
    print('O seu aumento de salário foi de 20%')
    print('O valor do aumento foi de: R${:.2f}'.format(aumento))
    print('Seu salário no próximo contra-cheque será: R${:.2f}'.format((salario+aumento)))
elif salario > 280 and salario <= 700:
    aumento = salario*0.15
    print('Seu salário antes do reajuste era de: R${:.2f}'.format(salario))
    print('O seu aumento de salário foi de 15%')
    print('O valor do aumento foi de: R${:.2f}'.format(aumento))
    print('Seu salário no próximo contra-cheque será: R${:.2f}'.format((salario+aumento)))
elif salario > 700 and salario <= 1500:
    aumento = salario*0.1
    print('Seu salário antes do reajuste era de: R${:.2f}'.format(salario))
    print('O seu aumento de salário foi de 10%')
    print('O valor do aumento foi de: R${:.2f}'.format(aumento))
    print('Seu salário no próximo contra-cheque será: R${:.2f}'.format((salario+aumento)))
else:
    aumento = salario*0.05
    print('Seu salário antes do reajuste era de: R${:.2f}'.format(salario))
    print('O seu aumento de salário foi de 5%')
    print('O valor do aumento foi de: R${:.2f}'.format(aumento))
    print('Seu salário no próximo contra-cheque será: R${:.2f}'.format((salario+aumento)))