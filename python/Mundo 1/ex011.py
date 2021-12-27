comprimento = float(input('Qual o comprimento da parede? '))
largura = float(input('Qual a largura da parede? '))

area = comprimento * largura
print(f'A parede tem a deminsão de {comprimento}x{largura} e sua área é de {area}m².')

tinta = area / 2
print(f'Para pintar a parede, você precisará de {tinta:.2f}L de tinta.')