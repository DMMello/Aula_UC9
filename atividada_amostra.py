import pandas as pd
import numpy as np
import os
os.system('cls')  # Limpa a tela (apenas no Windows)

# Idades de 5 pessoas da mesma família
dados = pd.Series([5, 10, 12, 35, 38])

# Transforma os dados em um array numpy
conjunto_dados = np.array(dados)

# Exibe o conjunto de dados
print(f'Conjunto de dados: {conjunto_dados}')

# Calcula a média
media = conjunto_dados.mean()
print(f'Média: {media}')

# Calcula a variância
variancia = np.var(conjunto_dados)
print(f'Variância da série de dados: {variancia}')

# Desvio padrão (raiz quadrada da variância)
desvio_padrao = np.sqrt(variancia)
print(f'Desvio padrão da série de dados: {desvio_padrao}')

# Forma mais direta de calcular o desvio padrão
desvio_padrao_direto = np.std(conjunto_dados)
print(f'Desvio padrão (cálculo direto): {desvio_padrao_direto}')

# Distância entre a variância e a média (não é uma medida comum, mas calculada como solicitado)
distancia_var_media = variancia / (media ** 2)
print(f'Distância entre a variância e a média (variância / média^2): {distancia_var_media}')

# Coeficiente de variação (desvio padrão / média * 100)
coef_variacao = (desvio_padrao / media) * 100
print(f'Coeficiente de variação: {coef_variacao}%')

#variancia amostral
variancia_amostral = np.var(dados, ddof=1)
print(f'Variancia amostral: {variancia_amostral}')

#desvio padrao
desvio_padrao_amostral = np.std(dados, ddof=1)
print(f'Variancia amostral: {desvio_padrao_amostral}')

