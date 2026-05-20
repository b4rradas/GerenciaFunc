from database import conectar

def criar_tarefa(titulo, descricao, prioridade, prazo, funcionario_id, status="Pendente"):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO tarefas (titulo, descricao, prioridade, prazo, funcionario_id, status)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (titulo, descricao, prioridade, prazo, funcionario_id, status))

    conn.commit()
    conn.close()


def listar_tarefas():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT tarefas.id, tarefas.titulo, tarefas.prioridade, tarefas.prazo,
               tarefas.status, funcionarios.nome
        FROM tarefas
        LEFT JOIN funcionarios ON tarefas.funcionario_id = funcionarios.id
    """)

    dados = cursor.fetchall()
    conn.close()
    return dados


def atualizar_tarefa(id, titulo, descricao, prioridade, prazo, funcionario_id, status):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE tarefas
        SET titulo=?, descricao=?, prioridade=?, prazo=?, funcionario_id=?, status=?
        WHERE id=?
    """, (titulo, descricao, prioridade, prazo, funcionario_id, status, id))

    conn.commit()
    conn.close()


def deletar_tarefa(id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM tarefas WHERE id=?", (id,))
    conn.commit()
    conn.close()


def concluir_tarefa(id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("UPDATE tarefas SET status='Concluída' WHERE id=?", (id,))
    conn.commit()
    conn.close()