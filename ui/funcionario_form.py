import tkinter as tk
from tkinter import ttk

from backend.funcionarios import cadastrar_funcionario, atualizar_funcionario
from ui import tema


class FuncionarioFormFrame(tk.Frame):
    def __init__(self, master, dados=None):
        super().__init__(master, bg=tema.BG)

        self.dados = dados

        titulo = "Editar Funcionário" if dados else "Cadastrar Funcionário"

        container = tk.Frame(self, bg=tema.BG)
        container.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(
            container,
            text=titulo,
            bg=tema.BG,
            fg=tema.ORANGE,
            font=tema.FONT_TITLE
        ).pack(pady=(0, 20))

        form = tema.card(container)
        form.pack()

        tema.label(form, "Nome").pack(anchor="w")
        self.nome = tema.entry(form)
        self.nome.pack(pady=(5, 15))

        tema.label(form, "Cargo").pack(anchor="w")
        self.cargo = tema.entry(form)
        self.cargo.pack(pady=(5, 15))

        tema.label(form, "Salário").pack(anchor="w")
        self.salario = tema.entry(form)
        self.salario.pack(pady=(5, 15))

        tema.label(form, "Status").pack(anchor="w")
        self.status = ttk.Combobox(
            form,
            values=["Ativo", "Inativo"],
            state="readonly",
            width=28
        )
        self.status.pack(pady=(5, 15))

        self.msg = tk.Label(
            form,
            text="",
            bg=tema.CARD,
            fg=tema.ERROR,
            font=tema.FONT_NORMAL
        )
        self.msg.pack(pady=(0, 10))

        tema.button(form, "Salvar", self.salvar).pack(pady=5)
        tema.button(form, "Cancelar", self.voltar, secondary=True).pack(pady=5)

        if dados:
            self.nome.insert(0, dados[1])
            self.cargo.insert(0, dados[2])
            self.salario.insert(0, dados[3])
            self.status.set(dados[4])
        else:
            self.status.set("Ativo")

    def salvar(self):
        nome = self.nome.get()
        cargo = self.cargo.get()
        salario = self.salario.get()
        status = self.status.get()

        if not nome or not cargo or not salario or not status:
            self.msg.config(text="Preencha todos os campos")
            return

        try:
            salario = float(salario)
        except ValueError:
            self.msg.config(text="Salário deve ser um número")
            return

        if self.dados:
            atualizar_funcionario(self.dados[0], nome, cargo, salario, status)
        else:
            cadastrar_funcionario(nome, cargo, salario, status)

        self.voltar()

    def voltar(self):
        from ui.funcionarios_ui import FuncionariosFrame
        self.master.trocar_tela(FuncionariosFrame)