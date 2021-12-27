nome = input('Digite seu nome completo: ')

print(f'Seu nome em maiúsculas: {nome.upper()}')
print(f'Seu nome em minúsculas: {nome.lower()}')
print(f'Quantidade de letras: {len(nome) - nome.count(" ")}')
print(f'Quantidade de letras do primeiro nome: {len(nome.split()[0])}')