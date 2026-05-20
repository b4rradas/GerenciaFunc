import tkinter as tk
from tkinter import ttk, filedialog, messagebox

from backend.funcionarios import listar_funcionarios, deletar_funcionario
from backend.exportar_funcionarios import exportar_funcionarios
from ui.importar_funcionarios_ui import ImportarFuncionariosWindow
from ui import tema


class FuncionariosFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg=tema.BG)

        tk.Label(
            self,
            text="Funcionários",
            bg=tema.BG,
            fg=tema.ORANGE,
            font=tema.FONT_TITLE
        ).pack(pady=20)

        self.configurar_tabela()

        self.tree = ttk.Treeview(
            self,
            columns=("ID", "Nome", "Cargo", "Salário", "Status"),
            show="headings",
            height=11
        )

        colunas = {
            "ID": 60,
            "Nome": 220,
            "Cargo": 180,
            "Salário": 120,
            "Status": 100
        }

        for col, largura in colunas.items():
            self.tree.heading(col, text=col)
            self.tree.column(col, width=largura, anchor="center")

        self.tree.pack(fill="x", padx=40, pady=10)

        frame_botoes = tk.Frame(self, bg=tema.BG)
        frame_botoes.pack(pady=15)

        tema.button(frame_botoes, "Adicionar", self.adicionar).grid(row=0, column=0, padx=5)
        tema.button(frame_botoes, "Editar", self.editar).grid(row=0, column=1, padx=5)
        tema.button(frame_botoes, "Remover", self.remover).grid(row=0, column=2, padx=5)
        tema.button(frame_botoes, "Importar", self.abrir_importacao).grid(row=0, column=3, padx=5)
        tema.button(frame_botoes, "Exportar", self.exportar).grid(row=0, column=4, padx=5)

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

        for f in listar_funcionarios():
            self.tree.insert("", "end", values=f)

    def adicionar(self):
        from ui.funcionario_form import FuncionarioFormFrame
        self.master.trocar_tela(FuncionarioFormFrame)

    def editar(self):
        selecionado = self.tree.selection()

        if not selecionado:
            self.msg.config(text="Selecione um funcionário para editar", fg=tema.ERROR)
            return

        dados = self.tree.item(selecionado)["values"]

        from ui.funcionario_form import FuncionarioFormFrame
        self.master.trocar_tela(lambda master: FuncionarioFormFrame(master, dados))

    def remover(self):
        selecionado = self.tree.selection()

        if not selecionado:
            self.msg.config(text="Selecione um funcionário para remover", fg=tema.ERROR)
            return

        dados = self.tree.item(selecionado)["values"]
        funcionario_id = dados[0]

        confirmar = messagebox.askyesno(
            "Confirmar remoção",
            f"Deseja remover o funcionário {dados[1]}?"
        )

        if confirmar:
            deletar_funcionario(funcionario_id)
            self.msg.config(text="Funcionário removido com sucesso", fg=tema.SUCCESS)
            self.atualizar_lista()

    def abrir_importacao(self):
        ImportarFuncionariosWindow(self, self.atualizar_lista)

    def exportar(self):
        caminho = filedialog.asksaveasfilename(
            defaultextension=".zip",
            filetypes=[("Arquivo ZIP", "*.zip")],
            initialfile="funcionarios.zip",
            title="Salvar funcionários"
        )

        if not caminho:
            return

        exportar_funcionarios(caminho)
        self.msg.config(text="Funcionários exportados com sucesso", fg=tema.SUCCESS)