import joblib

def optionTree():
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
  
def optionKnn(): 
  model = joblib.load('models/knn_Matheus_Souza.pkl')
  exemplo1 = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
  exemplo2 = [[1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
  exemplo3 = [[1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0]]
  exemplo4 = [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
  exemplo5 = [[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
  exemplo6 = [[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]]
  exemplo7 = [[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
  exemplo8 = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]
  exemplo9 = [[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]]
  predicted = model.predict(exemplo8)
  print(predicted[0])

print("Escolha qual modelo deseja usar:")
print("1 - Modelo de Árvore Binaria")
print("2 - Modelo de KNN")
opcao = int(input("Opção: "))

if opcao == 1:
  optionTree()

elif opcao == 2:
  optionKnn()