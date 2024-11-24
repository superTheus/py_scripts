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

    cursor.execute("SELECT * FROM iris_small")
    rows = cursor.fetchall()  
    conn.commit()
    cursor.close()
    conn.close()

    if len(rows) > 0:
      df = pd.DataFrame(rows, columns=['', 'sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)', 'classes'])
      df.to_excel('files/datasets/iris_small.xlsx', index=False)
      
    print("Dados Criados!")
else:
    print("Falha na conexão!")