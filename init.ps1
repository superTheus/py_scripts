$ENV_NAME = "amb"

if (Test-Path $ENV_NAME) {
    Write-Output "Ambiente virtual '$ENV_NAME' já existe."
}
else {
    python -m venv $ENV_NAME
    Write-Output "Ambiente virtual '$ENV_NAME' criado."
}

# Ativar o ambiente virtual
& "$ENV_NAME\Scripts\Activate.ps1"

# Instalar as dependências
pip install -r requirements.txt

Write-Output "Ambiente virtual '$ENV_NAME' criado e dependências instaladas."