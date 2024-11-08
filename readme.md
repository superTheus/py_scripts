# Create Dataset Script

Este repositório contém um script Python (`create_dataset.py`) que se conecta a um banco de dados MySQL e executa uma consulta para selecionar todos os dados da tabela `iris_small`.

## Pré-requisitos

Antes de executar o script, certifique-se de ter os seguintes itens instalados:

- Python 3.x
- MySQL Server
- Biblioteca `mysql-connector-python`

## Instalação

1. Clone este repositório para o seu ambiente local:
    ```sh
    git clone https://github.com/seu_usuario/seu_repositorio.git
    cd seu_repositorio
    ```

2. Execute o bash de inicialização do seu ambiente:
    ```sh
    python -m venv amb
    source amb/bin/activate  # No Windows use `amb\Scripts\activate`
    ```

3. Instale as dependências necessárias:
    ```sh
    pip install mysql-connector-python pandas
    ```

## Configuração

Antes de executar o script, edite o arquivo `create_dataset.py` para incluir as suas credenciais de conexão com o banco de dados MySQL:

```python
host = 'localhost'
database = 'datasets'
user = 'root'
password = 'sua_senha'
port = '3306'
```