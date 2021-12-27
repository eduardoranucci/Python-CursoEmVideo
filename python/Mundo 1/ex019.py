from random import choice

alunos = input('Digite o nome de quatro alunos: (Ex: Isa Ana Dre Bia) ').split()

print(f'Aluno sorteado é: {choice(alunos)}')