# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do
# Imposto de Renda, que depende do salário bruto (conforme tabela abaixo), 10% para o INSS,
# 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
# mas não é descontado (é a empresa que deposita).
# O Salário Líquido corresponde ao Salário Bruto menos os descontos.
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20%
# Imprima na tela as informações, dispostas conforme o exemplo abaixo.
# No exemplo o valor da hora é 5 e a quantidade de hora é 220.

# Inserção de variaveis
horas = int(input('Quantas horas você trabalhou no mês: '))
salario = float(input('Qual o valor do seu salário: R$'))

# Calculo de salário bruto e variaveis fixas
salarioBruto = horas*salario
fgts = salarioBruto*0.11
inss = salarioBruto*0.10
sind = salarioBruto*0.03

# Salario liquido
salarioLiquido = salarioBruto - inss - sind

# Estrutura condicional
if salarioBruto <= 900:
    print()
    print('Salário Bruto: ({:.2f}x{}): R${:.2f}'.format(salario, horas, salarioBruto))
    print('(-)IR: ISENTO')
    print('(-)Sindicato (3%): R${:.2f}'.format(sind))
    print('(-)INSS(10%): R${:.2f}'.format(inss))
    print('FGTS (11%): R${:.2f}'.format(fgts))
    print('Total de descontos: R${:.2f}'.format(inss+sind))
    print('Salário Liquido: R${:.2f}'.format(salarioLiquido))
elif salarioBruto > 900 and salarioBruto <= 1500:
    ir = salarioBruto*0.05
    print()
    print('Salário Bruto: ({:.2f}x{}): R${:.2f}'.format(salario, horas, salarioBruto))
    print('(-)IR(5%): R${:.2f}'.format(ir))
    print('(-)Sindicato (3%): R${:.2f}'.format(sind))
    print('(-)INSS(10%): R${:.2f}'.format(inss))
    print('FGTS (11%): R${:.2f}'.format(fgts))
    print('Total de descontos: R${:.2f}'.format(inss+sind+ir))
    print('Salario liquido :R${:.2f}'.format(salarioLiquido-ir))
elif salarioBruto > 1500 and salarioBruto <= 2500:
    ir = salarioBruto*0.1
    print()
    print('Salário Bruto: ({:.2f}x{}): R${:.2f}'.format(salario, horas, salarioBruto))
    print('(-)IR(10%): R${:.2f}'.format(ir))
    print('(-)Sindicato (3%): R${:.2f}'.format(sind))
    print('(-)INSS(10%): R${:.2f}'.format(inss))
    print('FGTS (11%): R${:.2f}'.format(fgts))
    print('Total de descontos: R${:.2f}'.format(inss+sind+ir))
    print('Salario liquido :R${:.2f}'.format(salarioLiquido-ir))
else:
    ir = salarioBruto*0.2
    print()
    print('Salário Bruto: ({:.2f}x{}): R${:.2f}'.format(salario, horas, salarioBruto))
    print('(-)IR(20%): R${:.2f}'.format(ir))
    print('(-)Sindicato (3%): R${:.2f}'.format(sind))
    print('(-)INSS(10%): R${:.2f}'.format(inss))
    print('FGTS (11%): R${:.2f}'.format(fgts))
    print('Total de descontos: R${:.2f}'.format(inss+sind+ir))
    print('Salario liquido :R${:.2f}'.format(salarioLiquido-ir))