import requests

from database import conectar


def importar_funcionarios(url):
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Erro ao acessar URL")

    dados = response.json()

    conn = conectar()
    cursor = conn.cursor()

    for funcionario in dados:
        cursor.execute("""
            INSERT INTO funcionarios (
                nome,
                cargo,
                salario,
                status
            )
            VALUES (?, ?, ?, ?)
        """, (
            funcionario["nome"],
            funcionario["cargo"],
            funcionario["salario"],
            funcionario["status"]
        ))

    conn.commit()
    conn.close()