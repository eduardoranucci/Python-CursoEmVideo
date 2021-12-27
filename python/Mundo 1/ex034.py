salario = float(input('Qual o seu salário? '))

if salario > 1250: print(f'Seu novo salário é: {(salario * 0.10) + salario}')
else: print(f'Seu novo salário é: {(salario * 0.15) + salario}')