import pandas as pd
import mysql.connector

host = 'localhost'
database = 'datasets'
user = 'root'
password = ''
port = '3306'

conn = mysql.connector.connect(
    host=host,
    database=database,
    user=user,
    password=password,
    port=port
)

if conn.is_connected():
    print("Conectado com sucesso!")
    cursor = conn.cursor()

    conjunto_dados = pd.read_csv("./files/datasets/iris_small.csv", index_col=0)

    for index, row in conjunto_dados.iterrows():
      cursor.execute(
          "INSERT INTO iris_small (sepal_length, sepal_width, petal_length, classes) VALUES (%s, %s, %s, %s)",
          (float(row['sepal length (cm)']), float(row['sepal width (cm)']), float(row['petal length (cm)']), float(row['classes']))
      )
        
    conn.commit()
    cursor.close()
    conn.close()
    
    print("Dados Criados!")
else:
    print("Falha na conexão!")