import tkinter as tk

from backend.importar_funcionarios import importar_funcionarios
from ui import tema


class ImportarFuncionariosWindow(tk.Toplevel):
    def __init__(self, master, atualizar_callback):
        super().__init__(master)

        self.atualizar_callback = atualizar_callback

        self.title("Importar Funcionários")
        self.geometry("520x260")
        self.configure(bg=tema.BG)
        self.resizable(False, False)

        container = tk.Frame(self, bg=tema.BG)
        container.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(
            container,
            text="Importar Funcionários",
            bg=tema.BG,
            fg=tema.ORANGE,
            font=tema.FONT_TITLE
        ).pack(pady=(0, 15))

        form = tema.card(container)
        form.pack()

        tk.Label(
            form,
            text="Endereço web do JSON",
            bg=tema.CARD,
            fg=tema.TEXT,
            font=tema.FONT_NORMAL
        ).pack(anchor="w")

        self.url = tk.Entry(
            form,
            bg="#262626",
            fg=tema.TEXT,
            insertbackground=tema.TEXT,
            relief="flat",
            font=tema.FONT_NORMAL,
            width=48
        )
        self.url.pack(pady=(5, 15))

        self.msg = tk.Label(
            form,
            text="",
            bg=tema.CARD,
            fg=tema.ERROR,
            font=tema.FONT_NORMAL
        )
        self.msg.pack(pady=(0, 10))

        tema.button(form, "Importar", self.importar).pack(pady=5)

    def importar(self):
        url = self.url.get()

        if not url:
            self.msg.config(text="Informe o endereço web do JSON", fg=tema.ERROR)
            return

        try:
            importar_funcionarios(url)
            self.msg.config(text="Funcionários importados com sucesso", fg=tema.SUCCESS)
            self.atualizar_callback()

        except Exception as erro:
            self.msg.config(text=f"Erro ao importar: {erro}", fg=tema.ERROR)