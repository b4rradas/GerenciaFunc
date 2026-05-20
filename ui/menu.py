import tkinter as tk
from ui import tema


class MenuFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg=tema.BG)

        user = self.master.usuario_logado
        nome_empresa = user[3]

        header = tk.Frame(self, bg=tema.BG)
        header.pack(fill="x", padx=40, pady=30)

        tk.Label(
            header,
            text="GerenciaFunc",
            bg=tema.BG,
            fg=tema.ORANGE,
            font=tema.FONT_TITLE
        ).pack(anchor="w")

        tk.Label(
            header,
            text=f"Empresa: {nome_empresa}",
            bg=tema.BG,
            fg=tema.MUTED,
            font=tema.FONT_NORMAL
        ).pack(anchor="w", pady=(5, 0))

        container = tk.Frame(self, bg=tema.BG)
        container.pack(expand=True)

        card = tema.card(container)
        card.pack()

        tk.Label(
            card,
            text="Menu Principal",
            bg=tema.CARD,
            fg=tema.TEXT,
            font=tema.FONT_SUBTITLE
        ).pack(pady=(0, 20))

        tema.button(card, "Funcionários", self.ir_funcionarios).pack(pady=6)
        tema.button(card, "Tarefas", self.ir_tarefas).pack(pady=6)
        tema.button(card, "Presença", self.ir_presenca).pack(pady=6)
        tema.button(card, "Sobre", self.ir_sobre).pack(pady=6)

        tk.Frame(card, bg=tema.CARD, height=15).pack()

        tema.button(card, "Sair", self.logout, secondary=True).pack(pady=6)

    def ir_funcionarios(self):
        from ui.funcionarios_ui import FuncionariosFrame
        self.master.trocar_tela(FuncionariosFrame)

    def ir_tarefas(self):
        from ui.tarefas_ui import TarefasFrame
        self.master.trocar_tela(TarefasFrame)

    def ir_presenca(self):
        from ui.presenca_ui import PresencaFrame
        self.master.trocar_tela(PresencaFrame)

    def ir_sobre(self):
        from ui.sobre import SobreFrame
        self.master.trocar_tela(SobreFrame)

    def logout(self):
        self.master.usuario_logado = None
        self.master.mostrar_login()