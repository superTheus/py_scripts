import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import accuracy_score
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn import tree
import joblib

datas = pd.read_csv("./files/datasets/tips_sample.csv")
datas.reset_index(inplace=True)
name_atributes = datas.columns[:6]

x = datas.drop(columns=['size'])
y = datas['size']

col_categorical = x.select_dtypes(include=['object']).columns
col_numerical = x.select_dtypes(include=['float64', 'int64']).columns

process = ColumnTransformer(
  transformers=[
    ('num', 'passthrough', col_numerical),
    ('cat', OneHotEncoder(), col_categorical)
  ]
)

atributes = datas[name_atributes]
labels = datas['size']

X_train, X_test, y_train, y_test = train_test_split(atributes, labels, test_size=0.3, random_state=13)

model = DecisionTreeClassifier(max_depth=None, random_state=13)
model.fit(X_train, y_train)

predicted = model.predict(X_train)
ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(y_train, predicted)).plot()
plt.grid(False)
plt.show()

predicted = model.predict(X_train)
accuracy = accuracy_score(predicted, y_train)

print(f'Acurária: {accuracy}')

predicted = model.predict(X_test)
accuracy = accuracy_score(predicted, y_test)

print(f'Acurária: {accuracy}')