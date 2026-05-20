import tkinter as tk
import calendar
from datetime import datetime

from backend.presenca import listar_presencas_por_dia
from ui import tema


class PresencaFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg=tema.BG)

        self.ano = datetime.now().year
        self.mes = datetime.now().month
        self.dia_selecionado = None

        tk.Label(
            self,
            text="Calendário de Presença",
            bg=tema.BG,
            fg=tema.ORANGE,
            font=tema.FONT_TITLE
        ).pack(pady=(12, 8))

        self.card_calendario = tema.card(self)
        self.card_calendario.configure(padx=20, pady=15)
        self.card_calendario.pack(pady=5)

        self.frame_topo = tk.Frame(self.card_calendario, bg=tema.CARD)
        self.frame_topo.pack(pady=(0, 8), fill="x")

        tk.Button(
            self.frame_topo,
            text="←",
            command=self.mes_anterior,
            bg=tema.CARD,
            fg=tema.TEXT,
            activebackground=tema.ORANGE_DARK,
            activeforeground=tema.TEXT,
            relief="flat",
            bd=0,
            font=tema.FONT_BUTTON,
            cursor="hand2",
            width=5
        ).pack(side="left", padx=5)

        self.label_mes = tk.Label(
            self.frame_topo,
            text="",
            bg=tema.CARD,
            fg=tema.ORANGE,
            font=tema.FONT_SUBTITLE
        )
        self.label_mes.pack(side="left", expand=True)

        tk.Button(
            self.frame_topo,
            text="→",
            command=self.proximo_mes,
            bg=tema.CARD,
            fg=tema.TEXT,
            activebackground=tema.ORANGE_DARK,
            activeforeground=tema.TEXT,
            relief="flat",
            bd=0,
            font=tema.FONT_BUTTON,
            cursor="hand2",
            width=5
        ).pack(side="right", padx=5)

        self.frame_dias = tk.Frame(self.card_calendario, bg=tema.CARD)
        self.frame_dias.pack()

        self.frame_info = tema.card(self)
        self.frame_info.configure(padx=20, pady=15)
        self.frame_info.pack(pady=8)

        tema.button(
            self,
            "Voltar",
            self.master.mostrar_menu,
            secondary=True
        ).pack(pady=(0, 8))

        self.desenhar_calendario()

    def desenhar_calendario(self):
        for widget in self.frame_dias.winfo_children():
            widget.destroy()

        meses = [
            "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
            "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
        ]

        self.label_mes.config(text=f"{meses[self.mes - 1]} de {self.ano}")

        dias_semana = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"]

        for col, dia in enumerate(dias_semana):
            tk.Label(
                self.frame_dias,
                text=dia,
                bg=tema.CARD,
                fg=tema.ORANGE,
                font=tema.FONT_BUTTON,
                width=6
            ).grid(row=0, column=col, padx=2, pady=2)

        calendario = calendar.monthcalendar(self.ano, self.mes)

        for linha, semana in enumerate(calendario, start=1):
            for coluna, dia in enumerate(semana):
                if dia == 0:
                    tk.Label(
                        self.frame_dias,
                        text="",
                        bg=tema.CARD,
                        width=6,
                        height=1
                    ).grid(row=linha, column=coluna, padx=2, pady=2)
                else:
                    tk.Button(
                        self.frame_dias,
                        text=str(dia),
                        bg=tema.BG,
                        fg=tema.TEXT,
                        activebackground=tema.ORANGE_DARK,
                        activeforeground=tema.TEXT,
                        relief="flat",
                        width=6,
                        height=1,
                        cursor="hand2",
                        command=lambda d=dia: self.selecionar_dia(d)
                    ).grid(row=linha, column=coluna, padx=2, pady=2)

    def selecionar_dia(self, dia):
        self.dia_selecionado = f"{dia:02d}-{self.mes:02d}-{self.ano}"
        self.mostrar_dados_do_dia()

    def mostrar_dados_do_dia(self):
        for widget in self.frame_info.winfo_children():
            widget.destroy()

        tk.Label(
            self.frame_info,
            text=f"Registros do dia {self.dia_selecionado}",
            bg=tema.CARD,
            fg=tema.ORANGE,
            font=tema.FONT_SUBTITLE
        ).pack(pady=(0, 8))

        registros = listar_presencas_por_dia(self.dia_selecionado)

        area_scroll = tk.Frame(self.frame_info, bg=tema.CARD)
        area_scroll.pack(fill="both")

        canvas = tk.Canvas(
            area_scroll,
            bg=tema.CARD,
            highlightthickness=0,
            width=560,
            height=130
        )
        canvas.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(
            area_scroll,
            orient="vertical",
            command=canvas.yview
        )
        scrollbar.pack(side="right", fill="y")

        canvas.configure(yscrollcommand=scrollbar.set)

        conteudo = tk.Frame(canvas, bg=tema.CARD)
        canvas.create_window((0, 0), window=conteudo, anchor="nw")

        def atualizar_scroll(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        conteudo.bind("<Configure>", atualizar_scroll)

        if not registros:
            tk.Label(
                conteudo,
                text="Nenhum funcionário registrado neste dia.",
                bg=tema.CARD,
                fg=tema.MUTED,
                font=tema.FONT_NORMAL
            ).pack(pady=5, anchor="w")
        else:
            for registro in registros:
                texto = (
                    f"Funcionário: {registro[0]}\n"
                    f"Descrição: {registro[1]}\n"
                    f"Horário: {registro[2]} até {registro[3]}"
                )

                tk.Label(
                    conteudo,
                    text=texto,
                    bg="#262626",
                    fg=tema.TEXT,
                    font=tema.FONT_NORMAL,
                    justify="left",
                    padx=12,
                    pady=8,
                    width=62,
                    anchor="w"
                ).pack(fill="x", pady=4)

        tema.button(
            self.frame_info,
            "Adicionar funcionário",
            self.ir_adicionar
        ).pack(pady=(10, 0))

    def ir_adicionar(self):
        if not self.dia_selecionado:
            return

        from ui.presenca_form import PresencaFormFrame
        self.master.trocar_tela(
            lambda master: PresencaFormFrame(master, self.dia_selecionado)
        )

    def mes_anterior(self):
        self.mes -= 1

        if self.mes == 0:
            self.mes = 12
            self.ano -= 1

        self.desenhar_calendario()

    def proximo_mes(self):
        self.mes += 1

        if self.mes == 13:
            self.mes = 1
            self.ano += 1

        self.desenhar_calendario()