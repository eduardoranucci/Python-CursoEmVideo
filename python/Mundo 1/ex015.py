dias = float(input('Quantos dias alugados? '))
km = float(input('Quantos KM rodados? '))

print(f'\nO total a pagar é R${(dias * 60) + (km * 0.15):.2f}')