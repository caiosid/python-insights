# Passo a passo
# Passo 1: Importar a base de dados
import pandas as pd

tabela = pd.read_csv('cancelamentos_sample.csv')

# Passo 2: Visualizar a base de dados (entender a base + identificar problemas)
# informações que não te ajudam, atrapalham
# CustomerID

tabela = tabela.drop(columns="CustomerID")
print(tabela)


# Passo 3: Corrigir os problemas da base de dados (tratamento de dados)
# valores vazios -> deletar linhas que tem valores vazios
print(tabela.info())

tabela = tabela.dropna() # NaN -> Not a Number = valores vazios

print(tabela.info())

# float -> numero com casa decimal
# object -> coluna com valores de texto 


# Passo 4: Análise Inicial -> quantos clientes cancelaram e qual o % de clientes
print(tabela['cancelou'].value_counts())


# Passo 5: Análise de causa de cancelamento dos clientes
# (comparar as outras colunas da tabela com a coluna de cancelamento)