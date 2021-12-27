km = int(input('Qual a velocidade do carro? '))

if km > 80:
    print(f'Você excedeu o limite de velocidade, a multa é de: R${(km - 80) * 7}')
    
else:
    print('Tudo certo!')