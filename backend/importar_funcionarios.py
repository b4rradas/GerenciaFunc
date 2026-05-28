import requests
from database import conectar


def normalizar_status(status):
    status = str(status).strip().lower()

    if status == "ativo":
        return "Ativo"

    if status == "inativo":
        return "Inativo"

    return "Ativo"


def importar_funcionarios(url):
    response = requests.get(url, timeout=10)

    if response.status_code != 200:
        raise Exception("Erro ao acessar URL")

    dados = response.json()

    if not isinstance(dados, list):
        raise Exception("O JSON precisa ser uma lista de funcionários")

    conn = conectar()
    cursor = conn.cursor()

    for funcionario in dados:
        nome = funcionario.get("nome")
        cargo = funcionario.get("cargo")
        salario = funcionario.get("salario")
        status = normalizar_status(funcionario.get("status", "Ativo"))

        if not nome or not cargo or salario is None:
            continue

        cursor.execute("""
            INSERT INTO funcionarios (nome, cargo, salario, status)
            VALUES (?, ?, ?, ?)
        """, (nome, cargo, float(salario), status))

    conn.commit()
    conn.close()