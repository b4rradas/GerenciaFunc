import tkinter as tk
from tkinter import ttk, messagebox

from backend.tarefas import listar_tarefas, deletar_tarefa, concluir_tarefa
from ui import tema


class TarefasFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg=tema.BG)

        tk.Label(
            self,
            text="Tarefas",
            bg=tema.BG,
            fg=tema.ORANGE,
            font=tema.FONT_TITLE
        ).pack(pady=20)

        self.configurar_tabela()

        frame_filtros = tk.Frame(self, bg=tema.BG)
        frame_filtros.pack(pady=5)

        tk.Label(
            frame_filtros,
            text="Importância:",
            bg=tema.BG,
            fg=tema.TEXT,
            font=tema.FONT_NORMAL
        ).grid(row=0, column=0, padx=5)

        self.filtro_prioridade = ttk.Combobox(
            frame_filtros,
            values=["", "Alta", "Média", "Baixa"],
            state="readonly",
            width=15
        )
        self.filtro_prioridade.grid(row=0, column=1, padx=5)

        tk.Label(
            frame_filtros,
            text="Prazo:",
            bg=tema.BG,
            fg=tema.TEXT,
            font=tema.FONT_NORMAL
        ).grid(row=0, column=2, padx=5)

        self.filtro_prazo = tema.entry(frame_filtros)
        self.filtro_prazo.config(width=18)
        self.filtro_prazo.grid(row=0, column=3, padx=5)

        tema.button(frame_filtros, "Filtrar", self.atualizar_lista).grid(row=0, column=4, padx=5)
        tema.button(frame_filtros, "Limpar", self.limpar_filtros, secondary=True).grid(row=0, column=5, padx=5)

        self.tree = ttk.Treeview(
            self,
            columns=("ID", "Título", "Prioridade", "Prazo", "Status", "Funcionário"),
            show="headings",
            height=10
        )

        colunas = {
            "ID": 60,
            "Título": 220,
            "Prioridade": 120,
            "Prazo": 120,
            "Status": 130,
            "Funcionário": 180
        }

        for col, largura in colunas.items():
            self.tree.heading(col, text=col)
            self.tree.column(col, width=largura, anchor="center")

        self.tree.pack(fill="x", padx=40, pady=15)

        frame_botoes = tk.Frame(self, bg=tema.BG)
        frame_botoes.pack(pady=10)

        tema.button(frame_botoes, "Criar", self.criar).grid(row=0, column=0, padx=5)
        tema.button(frame_botoes, "Editar", self.editar).grid(row=0, column=1, padx=5)
        tema.button(frame_botoes, "Remover", self.remover).grid(row=0, column=2, padx=5)
        tema.button(frame_botoes, "Concluir", self.concluir).grid(row=0, column=3, padx=5)

        self.msg = tk.Label(
            self,
            text="",
            bg=tema.BG,
            fg=tema.SUCCESS,
            font=tema.FONT_NORMAL
        )
        self.msg.pack(pady=5)

        tema.button(self, "Voltar", self.master.mostrar_menu, secondary=True).pack(pady=10)

        self.atualizar_lista()

    def configurar_tabela(self):
        style = ttk.Style()
        style.theme_use("default")

        style.configure(
            "Treeview",
            background="#1E1E1E",
            foreground=tema.TEXT,
            fieldbackground="#1E1E1E",
            rowheight=28,
            font=tema.FONT_NORMAL
        )

        style.configure(
            "Treeview.Heading",
            background=tema.ORANGE,
            foreground=tema.TEXT,
            font=tema.FONT_BUTTON
        )

        style.map(
            "Treeview",
            background=[("selected", tema.ORANGE_DARK)]
        )

    def atualizar_lista(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        prioridade = self.filtro_prioridade.get()
        prazo = self.filtro_prazo.get()

        for tarefa in listar_tarefas():
            if prioridade and tarefa[2] != prioridade:
                continue

            if prazo and tarefa[3] != prazo:
                continue

            self.tree.insert("", "end", values=tarefa)

    def limpar_filtros(self):
        self.filtro_prioridade.set("")
        self.filtro_prazo.delete(0, tk.END)
        self.atualizar_lista()

    def criar(self):
        from ui.tarefa_form import TarefaFormFrame
        self.master.trocar_tela(TarefaFormFrame)

    def editar(self):
        selecionado = self.tree.selection()

        if not selecionado:
            self.msg.config(text="Selecione uma tarefa para editar", fg=tema.ERROR)
            return

        dados = self.tree.item(selecionado)["values"]

        from ui.tarefa_form import TarefaFormFrame
        self.master.trocar_tela(lambda master: TarefaFormFrame(master, dados))

    def remover(self):
        selecionado = self.tree.selection()

        if not selecionado:
            self.msg.config(text="Selecione uma tarefa para remover", fg=tema.ERROR)
            return

        dados = self.tree.item(selecionado)["values"]
        tarefa_id = dados[0]

        confirmar = messagebox.askyesno(
            "Confirmar remoção",
            f"Deseja remover a tarefa {dados[1]}?"
        )

        if confirmar:
            deletar_tarefa(tarefa_id)
            self.msg.config(text="Tarefa removida com sucesso", fg=tema.SUCCESS)
            self.atualizar_lista()

    def concluir(self):
        selecionado = self.tree.selection()

        if not selecionado:
            self.msg.config(text="Selecione uma tarefa para concluir", fg=tema.ERROR)
            return

        dados = self.tree.item(selecionado)["values"]
        tarefa_id = dados[0]

        concluir_tarefa(tarefa_id)
        self.msg.config(text="Tarefa concluída com sucesso", fg=tema.SUCCESS)
        self.atualizar_lista()