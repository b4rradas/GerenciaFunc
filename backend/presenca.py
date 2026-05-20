from database import conectar

def registrar_presenca(funcionario_id, dia, descricao, hora_inicio, hora_fim):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO presenca (funcionario_id, dia, descricao, hora_inicio, hora_fim)
        VALUES (?, ?, ?, ?, ?)
    """, (funcionario_id, dia, descricao, hora_inicio, hora_fim))

    conn.commit()
    conn.close()


def listar_presencas_por_dia(dia):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT funcionarios.nome, presenca.descricao, presenca.hora_inicio, presenca.hora_fim
        FROM presenca
        LEFT JOIN funcionarios ON presenca.funcionario_id = funcionarios.id
        WHERE presenca.dia = ?
    """, (dia,))

    dados = cursor.fetchall()
    conn.close()
    return dados