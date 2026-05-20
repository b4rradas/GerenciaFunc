import tkinter as tk
from database import criar_tabelas
from ui import tema


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Sistema Empresa")
        self.geometry("900x600")
        self.minsize(900, 600)
        self.configure(bg=tema.BG)

        self.frame_atual = None
        self.usuario_logado = None

        self.mostrar_login()

    def trocar_tela(self, FrameClass):
        if self.frame_atual is not None:
            self.frame_atual.destroy()

        self.frame_atual = FrameClass(self)
        self.frame_atual.pack(fill="both", expand=True)

    def mostrar_login(self):
        from ui.login import LoginFrame
        self.trocar_tela(LoginFrame)

    def mostrar_menu(self):
        from ui.menu import MenuFrame
        self.trocar_tela(MenuFrame)


def main():
    criar_tabelas()
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()