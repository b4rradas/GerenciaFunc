from database import conectar

def cadastrar_funcionario(nome, cargo, salario, status):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO funcionarios (nome, cargo, salario, status)
        VALUES (?, ?, ?, ?)
    """, (nome, cargo, salario, status))

    conn.commit()
    conn.close()


def listar_funcionarios():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM funcionarios")
    dados = cursor.fetchall()

    conn.close()
    return dados


def deletar_funcionario(id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM funcionarios WHERE id=?", (id,))

    conn.commit()
    conn.close()

def atualizar_funcionario(id, nome, cargo, salario, status):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE funcionarios
        SET nome=?, cargo=?, salario=?, status=?
        WHERE id=?
    """, (nome, cargo, salario, status, id))

    conn.commit()
    conn.close()