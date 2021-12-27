from random import shuffle

alunos = input('Digite o nome de quatro alunos: (Ex: Isa Ana Dre Bia) ').split()

shuffle(alunos)

print(f'A ordem de apresentação é: {alunos}')