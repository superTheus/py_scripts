import pandas as pd
dataset = pd.read_csv('files/datasets/dataset_esrb.csv')

train = dataset.sample(frac=0.8, random_state=0)
test = dataset.drop(train.index)

test.to_csv('files/datasets/teste_esrb.csv', index=False)
train.to_csv('files/datasets/treino_esrb.csv', index=False)