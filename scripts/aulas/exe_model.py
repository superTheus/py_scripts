import joblib
model = joblib.load('models/modelo_joao_matheus.pkl')

print("Informa o valor do tamanho da sépala, largura da sépala e tamanho da pétala")
sepal_length = float(input("Tamanho da sépala: "))
sepal_width = float(input("Largura da sépala: "))
petal_length = float(input("Tamanho da pétala: "))
petal_width = float(input("Largura da pétala: "))

exemplo = [[sepal_length, sepal_width, petal_length, petal_width]]
predicted = model.predict(exemplo)
target_names = ['setosa', 'versicolor', 'virginica']

print("Predição:", target_names[predicted[0]])