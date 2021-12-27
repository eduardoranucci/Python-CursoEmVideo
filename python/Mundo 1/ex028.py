from random import randint

print('Vou pensar em um número de 0 a 5, tente adivinhar!')

num_escolhido = randint(0, 5)

num_jogador = int(input('Em qual número eu pensei? '))

if num_escolhido == num_jogador: print('Você acertou!')   
else: print(f'Você errou! o número certo era: {num_escolhido}')