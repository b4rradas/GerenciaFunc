import tkinter as tk
from tkinter import ttk

from backend.tarefas import criar_tarefa, atualizar_tarefa
from backend.funcionarios import listar_funcionarios
from ui import tema


class TarefaFormFrame(tk.Frame):
    def __init__(self, master, dados=None):
        super().__init__(master, bg=tema.BG)

        self.dados = dados

        titulo = "Editar Tarefa" if dados else "Criar Tarefa"

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

        tema.label(form, "Título").pack(anchor="w")
        self.titulo = tema.entry(form)
        self.titulo.pack(pady=(5, 15))

        tema.label(form, "Descrição").pack(anchor="w")
        self.descricao = tk.Text(
            form,
            width=30,
            height=4,
            bg="#262626",
            fg=tema.TEXT,
            insertbackground=tema.TEXT,
            relief="flat",
            font=tema.FONT_NORMAL
        )
        self.descricao.pack(pady=(5, 15))

        tema.label(form, "Nível de importância").pack(anchor="w")
        self.prioridade = ttk.Combobox(
            form,
            values=["Alta", "Média", "Baixa"],
            state="readonly",
            width=28
        )
        self.prioridade.pack(pady=(5, 15))

        tema.label(form, "Prazo (YYYY-MM-DD)").pack(anchor="w")
        self.prazo = tema.entry(form)
        self.prazo.pack(pady=(5, 15))

        funcionarios = listar_funcionarios()

        tema.label(form, "Funcionário atribuído").pack(anchor="w")
        self.funcionario = ttk.Combobox(
            form,
            values=[f"{f[0]} - {f[1]}" for f in funcionarios],
            state="readonly",
            width=28
        )
        self.funcionario.pack(pady=(5, 15))

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
            self.titulo.insert(0, dados[1])
            self.prioridade.set(dados[2])
            self.prazo.insert(0, dados[3])
        else:
            self.prioridade.set("Média")

    def salvar(self):
        titulo = self.titulo.get()
        descricao = self.descricao.get("1.0", tk.END).strip()
        prioridade = self.prioridade.get()
        prazo = self.prazo.get()
        funcionario = self.funcionario.get()

        if not titulo or not descricao or not prioridade or not prazo or not funcionario:
            self.msg.config(text="Preencha todos os campos")
            return

        funcionario_id = int(funcionario.split(" - ")[0])

        if self.dados:
            atualizar_tarefa(
                self.dados[0],
                titulo,
                descricao,
                prioridade,
                prazo,
                funcionario_id,
                "Pendente"
            )
        else:
            criar_tarefa(
                titulo,
                descricao,
                prioridade,
                prazo,
                funcionario_id
            )

        self.voltar()

    def voltar(self):
        from ui.tarefas_ui import TarefasFrame
        self.master.trocar_tela(TarefasFrame)