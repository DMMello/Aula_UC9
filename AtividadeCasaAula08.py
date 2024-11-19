import pandas as pd
import numpy as np

# obter dados / CSV vendas 2017 miranda
try:
    print('Obtendo dados...')
    df_dados_vendas = pd.read_csv( 
        'tb_Vendas2017_Miranda.csv', sep=';', encoding='iso-8859-1')

#selecionando somente as variaveis:
    df_vendas = df_dados_vendas(['Numero de vendas', 'ID Produto','Id Cliente', 'Quantidade Vendida'])

print(df_vendas.head())
