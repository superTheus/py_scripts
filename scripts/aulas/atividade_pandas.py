import pandas as pd

dados = pd.read_csv("./files/datasets/tips_sample.csv", index_col=0)
dados.reset_index(inplace=True)

print('--- Questão 01 ---')
print('a - \n', dados.tail(3))

print('--- Questão 02 ---')
print('a - \n', dados[['sex', 'smoker']])
print('b - \n',dados.iloc[:5][['total_bill', 'tip']])
print('c - \n',dados.loc[dados['day'] == 'Sun'])

print('--- Questão 03 ---')
print('a - \n', dados.query("total_bill > 30 and tip > 5"))
print('b - \n', dados.query("day == 'Sat' and size > 2"))

print('--- Questão 04 ---')
print('a - \n', dados[['total_bill', 'tip']].mean())
print('b - \n', dados['time'].unique())
print('c - \n', dados['tip'].sum())

print('--- Questão 05 ---')

dados['taxa_servico'] = dados['tip'] / dados['size']
print('a - \n', dados)
dados = dados.drop(columns=['sex'])
print('b - \n', dados)
print('b - \n', dados.isna().sum())