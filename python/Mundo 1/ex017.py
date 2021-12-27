from math import hypot

cateto_oposto = float(input('Qual o valor do cateto oposto? '))
cateto_adjacente = float(input('Qual o valor do cateto adjacente? '))

print(f'\nO valor da hipotenusa é: {hypot(cateto_oposto, cateto_adjacente):.2f}')