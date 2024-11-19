import pandas as pd 
import numpy as np 
import os
os.system('cls')

# calcule a variancia entre a idade de 5 pessoas da mesma familia
dados = pd.Series([5,10,12,35,38])

#trasmforma os dados em array numpy
conjunto_dados = np.array(dados)

print(f'Conjunto de dados: {conjunto_dados}')

#calcula a media
print(f'Media: {conjunto_dados.mean()}')

#calcula a variancia
print(f'Variancia da da Serie de dados: {np.var(conjunto_dados)}')

# #desvio padrao
# # o desvio padrao eh a raiz quadrada da variancia
print(f'Desvio Padrao da serie de dados: {np.sqrt(conjunto_dados.var())}')

# #forma mais direta de calcular o desvio padrao 
# #calcula diretamente o desvio padrao do conjunto de dedos
print(f'Desvio padrao da seria de dados {np.std(conjunto_dados)}')


