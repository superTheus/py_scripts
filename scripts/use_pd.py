import pandas as pd
import time

dados = pd.read_csv("./files/datasets/tips_sample.csv", index_col=0)
dados.reset_index(inplace=True)

# Selecionar uma coluna específica
col = dados['total_bill']
print(col)

# Selecionar múltiplas colunas
cols = dados[['total_bill', 'tip', 'sex']]
print(cols)

# Filtrar os dados para exibir apenas as linhas onde o valor da conta total (total_bill) é maior que 20
print(dados.query("total_bill > 20 and sex == 'Female'"))


print(dados.query("tip > 3 and sex == 'Female'"))