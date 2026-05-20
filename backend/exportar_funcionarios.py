import json
import zipfile
import os

from database import conectar


def exportar_funcionarios(caminho_zip):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, nome, cargo, salario, status
        FROM funcionarios
    """)

    funcionarios = cursor.fetchall()

    conn.close()

    dados = []

    for f in funcionarios:
        dados.append({
            "id": f[0],
            "nome": f[1],
            "cargo": f[2],
            "salario": f[3],
            "status": f[4]
        })

    json_temp = "funcionarios_temp.json"

    with open(json_temp, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

    with zipfile.ZipFile(caminho_zip, "w") as zipf:
        zipf.write(json_temp, arcname="funcionarios.json")

    os.remove(json_temp)