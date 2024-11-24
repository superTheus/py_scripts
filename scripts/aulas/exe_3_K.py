import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import sys
import joblib

train = pd.read_csv('files/datasets/treino_esrb.csv')
test = pd.read_csv('files/datasets/teste_esrb.csv')

train.isnull().sum()
test.isnull().sum()

X_train = train.drop(["title","esrb_rating"] , axis=1)
y_train = train["esrb_rating"]

X_test =  test.drop(["title","esrb_rating"] , axis=1)
y_test = test["esrb_rating"]

array_acc = []
best_k = 0

for i in range(1, 20):
    print("K: \n", i)
    modelo = KNeighborsClassifier(n_neighbors=i)
    modelo.fit(X_train,y_train)
    predicoes = modelo.predict(X_test)
    acuracia_model = accuracy_score(y_test , predicoes)
    array_acc.append(acuracia_model)
    if acuracia_model == max(array_acc):
        best_k = i
  
print("Acurácia K: {}".format(round(max(array_acc)*100,4)))
print("Melhor K:", best_k)

modelo = KNeighborsClassifier(n_neighbors=best_k)
modelo.fit(X_train,y_train)
predicoes = modelo.predict(X_test)
acuracia_model = accuracy_score(y_test , predicoes)

print("Melhor Acurácia K: {}".format(round(acuracia_model*100,4)))

res = input("Deseja salvar o modelo? s/n: ")
if res == 's':
    joblib.dump(modelo, 'models/knn_Matheus_Souza.pkl')
    print("Modelo salvo com sucesso!")
else:
    sys.exit("Saída do programa")