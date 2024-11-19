dados = (1,2,3,4,5)

# calcula media
media = sum(dados) / len(dados)
print(f'Media: {media}')

#calcular as diferencas entre cada valor e a media
diferencas = [x - media for x in dados]
print(f'Diferecas entre relacao a media: {diferencas}')

#elevar as diferencas ao quadrado
quadrados_diferencas = [x**2 for x in diferencas]
print(f'Quadrados das diferencas: {quadrados_diferencas}')

#calcular a media dos quadrados das diferencas
media_quadrados_diferencas = sum(quadrados_diferencas) / len(quadrados_diferencas)
print(f'Variancia e a media dos quadrados das diferencas: {media_quadrados_diferencas}')

#calcular a raiz quadrada da media dos quadrados das diferencas
desvio_padrao = media_quadrados_diferencas ** 0.5
print(f'Desvio padrao e a raiz quadrada da variancia: {desvio_padrao}')