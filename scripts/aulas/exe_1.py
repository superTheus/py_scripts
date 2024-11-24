import pandas as pd
import time
import os
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import accuracy_score
from sklearn import tree
import joblib
import sys

os.system('cls' if os.name == 'nt' else 'clear')
conjunto_dados = pd.read_excel("./files/datasets/iris_small.xlsx", index_col=0)

nome_atributos = conjunto_dados.columns[:4]

atributos = conjunto_dados[nome_atributos]
rotulos = conjunto_dados["classes"]



# print("Atributos: ", atributos)
# print("Rotulos: ", rotulos)

# print("Rotulos: ", rotulos)
# time.sleep(2)
# os.system('cls' if os.name == 'nt' else 'clear')

X_train, X_test, y_train, y_test = train_test_split(atributos, 
                                                    rotulos, 
                                                    test_size=0.3, 
                                                    random_state=13)

# print("Treino: ")
# print(X_train)
# print(y_train)

# print("Teste: ")
# print(X_test)
# print(y_test)

# os.sys.exit("Saindo...")

model = DecisionTreeClassifier(max_depth=None, random_state = 13)
model.fit(X_train, y_train)

predicted = model.predict(X_train)
ConfusionMatrixDisplay(
    confusion_matrix=confusion_matrix(y_train, predicted)).plot()

plt.grid(False)
plt.show()

# predicted = model.predict(X_train)
# accuracy = accuracy_score(predicted, y_train)

# print(f'Acurária: {accuracy}')

# predicted = model.predict(X_test)
# accuracy = accuracy_score(predicted, y_test)

# print(f'Acurária: {accuracy}')

feature_names = [
    'sepal length (cm)',
    'sepal width (cm)',
    'petal length (cm)',
    'petal width (cm)',
]

target_names = ['setosa', 'versicolor', 'virginica']

fig = plt.figure(figsize = (10, 7))
tree.plot_tree(model,
               feature_names = feature_names,
               class_names = target_names, filled = True)
plt.show()

resposta = input("Deseja salvar o modelo treinado? (s/n): ")

if resposta == 's':
    joblib.dump(model, 'models/modelo_joao_matheus.pkl')
    print("Modelo salvo com sucesso!")