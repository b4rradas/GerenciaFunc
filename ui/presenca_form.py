import tkinter as tk
from tkinter import ttk

from backend.presenca import registrar_presenca
from backend.funcionarios import listar_funcionarios
from ui import tema


class PresencaFormFrame(tk.Frame):
    def __init__(self, master, dia):
        super().__init__(master, bg=tema.BG)

        self.dia = dia

        container = tk.Frame(self, bg=tema.BG)
        container.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(
            container,
            text=f"Adicionar Presença",
            bg=tema.BG,
            fg=tema.ORANGE,
            font=tema.FONT_TITLE
        ).pack(pady=(0, 5))

        tk.Label(
            container,
            text=f"Data: {dia}",
            bg=tema.BG,
            fg=tema.MUTED,
            font=tema.FONT_NORMAL
        ).pack(pady=(0, 20))

        form = tema.card(container)
        form.pack()

        funcionarios = listar_funcionarios()

        tema.label(form, "Funcionário").pack(anchor="w")
        self.funcionario = ttk.Combobox(
            form,
            values=[f"{f[0]} - {f[1]}" for f in funcionarios],
            state="readonly",
            width=28
        )
        self.funcionario.pack(pady=(5, 15))

        tema.label(form, "Descrição do trabalho").pack(anchor="w")
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

        tema.label(form, "Hora início").pack(anchor="w")
        self.hora_inicio = tema.entry(form)
        self.hora_inicio.insert(0, "00:00")
        self.hora_inicio.pack(pady=(5, 15))

        tema.label(form, "Hora fim").pack(anchor="w")
        self.hora_fim = tema.entry(form)
        self.hora_fim.insert(0, "00:00")
        self.hora_fim.pack(pady=(5, 15))

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

    def validar_hora(self, hora):
        if len(hora) != 5 or hora[2] != ":":
            return False

        h, m = hora.split(":")

        if not h.isdigit() or not m.isdigit():
            return False

        h = int(h)
        m = int(m)

        if h < 0 or h > 23:
            return False

        if m < 0 or m > 59:
            return False

        return True

    def mostrar_erro(self, texto):
        self.msg.config(text=texto, fg=tema.ERROR)

    def salvar(self):
        self.msg.config(text="")

        funcionario = self.funcionario.get()
        descricao = self.descricao.get("1.0", tk.END).strip()
        inicio = self.hora_inicio.get()
        fim = self.hora_fim.get()

        if not funcionario:
            self.mostrar_erro("Selecione um funcionário")
            return

        if not descricao:
            self.mostrar_erro("Informe a descrição do trabalho")
            return

        if not self.validar_hora(inicio) or not self.validar_hora(fim):
            self.mostrar_erro("Hora inválida! Use HH:MM")
            return

        if inicio >= fim:
            self.mostrar_erro("Hora início deve ser menor que hora fim")
            return

        funcionario_id = int(funcionario.split(" - ")[0])

        registrar_presenca(
            funcionario_id,
            self.dia,
            descricao,
            inicio,
            fim
        )

        self.voltar()

    def voltar(self):
        from ui.presenca_ui import PresencaFrame
        self.master.trocar_tela(PresencaFrame)