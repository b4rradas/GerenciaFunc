import tkinter as tk
from backend.auth import cadastrar_usuario
from ui import tema


class CadastroFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg=tema.BG)

        container = tk.Frame(self, bg=tema.BG)
        container.place(relx=0.5, rely=0.5, anchor="center")

        tema.title(container, "Cadastro").pack(pady=(0, 20))

        form = tema.card(container)
        form.pack()

        tema.label(form, "Usuário").pack(anchor="w")
        self.usuario = tema.entry(form)
        self.usuario.pack(pady=(5, 15))

        tema.label(form, "Senha").pack(anchor="w")
        self.senha = tema.entry(form, show="*")
        self.senha.pack(pady=(5, 15))

        tema.label(form, "Nome da empresa").pack(anchor="w")
        self.empresa = tema.entry(form)
        self.empresa.pack(pady=(5, 15))

        self.msg = tk.Label(
            form,
            text="",
            bg=tema.CARD,
            fg=tema.ERROR,
            font=tema.FONT_NORMAL
        )
        self.msg.pack(pady=(0, 10))

        tema.button(form, "Cadastrar", self.cadastrar).pack(pady=5)
        tema.button(form, "Voltar ao login", self.voltar, secondary=True).pack(pady=5)

    def cadastrar(self):
        usuario = self.usuario.get()
        senha = self.senha.get()
        empresa = self.empresa.get()

        if not usuario or not senha or not empresa:
            self.msg.config(text="Preencha todos os campos", fg=tema.ERROR)
            return

        if len(senha) < 8:
            self.msg.config(text="A senha deve ter pelo menos 8 caracteres", fg=tema.ERROR)
            return

        sucesso = cadastrar_usuario(usuario, senha, empresa)

        if sucesso:
            self.msg.config(text="Cadastro realizado com sucesso", fg=tema.SUCCESS)
        else:
            self.msg.config(text="Usuário já existe", fg=tema.ERROR)

    def voltar(self):
        self.master.mostrar_login()