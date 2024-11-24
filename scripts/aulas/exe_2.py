import pandas as pd
from sklearn.datasets import load_breast_cancer
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import accuracy_score
from sklearn import tree
import joblib
import sys
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score

colors=['#35b2de','#ffcb5a']


dataset = pd.read_csv('./files/datasets/breast_cancer.csv', index_col=0)

headers = dataset.drop(columns=['classes']).columns
rotulos = dataset['classes']
atributos = dataset[headers]

labels = rotulos.value_counts().index

res = input("Mostrar dados em gráfico? s/n: ")

if(res == 's'):
    plt.pie(rotulos.value_counts(), autopct='%1.1f%%', colors=colors)
    plt.legend(labels,bbox_to_anchor=(1.25,1),)
    plt.title('Porcentagem: Benignos x Malignos ')
    plt.show()


X_train, X_test, y_train, y_test = train_test_split(atributos, 
                                                    rotulos, 
                                                    test_size=0.3, 
                                                    random_state=13)

model = DecisionTreeClassifier(max_depth=None, random_state = 13)
model.fit(X_train, y_train)

res = input("Mostrar matriz de confusão? s/n: ")

if(res == 's'):
    predicted = model.predict(X_train)
    ConfusionMatrixDisplay(
        confusion_matrix=confusion_matrix(y_train, predicted)).plot()
    plt.grid(False)
    plt.show()

res = input("Mostrar árvore binária? s/n: ")

if(res == 's'):
    feature_names = headers
    class_names = ['Benigno', 'Maligno']
    fig = plt.figure(figsize = (10, 7))
    tree.plot_tree(model,
                feature_names = feature_names,
                class_names = class_names, filled = True)
    plt.show()

predicted = model.predict(X_test)

accuracy = accuracy_score(predicted, y_test)
precision = precision_score(y_test, predicted)
recall = recall_score(y_test, predicted)
f1 = f1_score(y_test, predicted)

print(f'Acurária: {accuracy:.2f}')
print(f'Precisão: {precision:.2f}')
print(f"Recall do modelo: {recall:.2f}")
print(f"F1: {f1:.2f}")

res = input("Deseja salvar o modelo? s/n: ")
if res == 's':
    joblib.dump(model, 'models/tree2_Matheus_Souza.pkl')
    print("Modelo salvo com sucesso!")
else:
    sys.exit("Saída do programa")