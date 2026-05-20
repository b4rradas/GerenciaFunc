import tkinter as tk
from ui import tema


class SobreFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg=tema.BG)

        container = tk.Frame(self, bg=tema.BG)
        container.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(
            container,
            text="Sobre o Projeto",
            bg=tema.BG,
            fg=tema.ORANGE,
            font=tema.FONT_TITLE
        ).pack(pady=(0, 20))

        card = tema.card(container)
        card.pack()

        texto = (
            "Tema:\n"
            "Sistema de Gerenciamento Empresarial\n\n"
            "Objetivo:\n"
            "Desenvolver uma aplicação desktop para auxiliar no gerenciamento de funcionários, "
            "controle de presença e organização de tarefas dentro de uma empresa. "
            "A proposta busca centralizar informações importantes, permitindo cadastrar, editar, "
            "remover e consultar funcionários, registrar presença com horários e descrições, "
            "atribuir tarefas com prazos e níveis de importância, além de importar e exportar dados.\n\n"
            "Desenvolvedor(es):\n"
            "Nome completo: Lucas Barradas Hisamitsu\n"
            "RA: 2840482321002"
        )

        tk.Label(
            card,
            text=texto,
            bg=tema.CARD,
            fg=tema.TEXT,
            font=tema.FONT_NORMAL,
            justify="left",
            wraplength=520
        ).pack(padx=10, pady=10)

        tema.button(card, "Voltar", self.master.mostrar_menu, secondary=True).pack(pady=(20, 0))