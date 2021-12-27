km = int(input('Digite a distância em KM da viajem: '))

if km <= 200:
    print(f'O valor da viajem será de: R${km * 0.50}')
else:
    print(f'O valor da viajem será de: R${km * 0.45}')