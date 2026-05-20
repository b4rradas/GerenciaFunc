import tkinter as tk
from backend.auth import login
from ui import tema


class LoginFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg=tema.BG)

        container = tk.Frame(self, bg=tema.BG)
        container.place(relx=0.5, rely=0.5, anchor="center")

        tema.title(container, "GerenciaFunc").pack(pady=(0, 5))

        tk.Label(
            container,
            text="Acesse sua empresa",
            bg=tema.BG,
            fg=tema.MUTED,
            font=tema.FONT_NORMAL
        ).pack(pady=(0, 20))

        form = tema.card(container)
        form.pack()

        tema.label(form, "Usuário").pack(anchor="w")
        self.usuario = tema.entry(form)
        self.usuario.pack(pady=(5, 15))

        tema.label(form, "Senha").pack(anchor="w")
        self.senha = tema.entry(form, show="*")
        self.senha.pack(pady=(5, 15))

        self.msg = tk.Label(
            form,
            text="",
            bg=tema.CARD,
            fg=tema.ERROR,
            font=tema.FONT_NORMAL
        )
        self.msg.pack(pady=(0, 10))

        tema.button(form, "Entrar", self.fazer_login).pack(pady=5)
        tema.button(form, "Criar conta", self.ir_cadastro, secondary=True).pack(pady=5)

    def fazer_login(self):
        user = login(self.usuario.get(), self.senha.get())

        if user:
            self.master.usuario_logado = user
            self.master.mostrar_menu()
        else:
            self.msg.config(text="Usuário ou senha inválidos")

    def ir_cadastro(self):
        from ui.cadastro import CadastroFrame
        self.master.trocar_tela(CadastroFrame)