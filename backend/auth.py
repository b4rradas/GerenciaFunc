from database import conectar

def cadastrar_usuario(usuario, senha, empresa):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios WHERE usuario = ?", (usuario,))
    if cursor.fetchone():
        conn.close()
        return False

    cursor.execute("""
        INSERT INTO usuarios (usuario, senha, nome_empresa)
        VALUES (?, ?, ?)
    """, (usuario, senha, empresa))

    conn.commit()
    conn.close()
    return True


def login(usuario, senha):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM usuarios WHERE usuario = ? AND senha = ?
    """, (usuario, senha))

    user = cursor.fetchone()
    conn.close()
    return user