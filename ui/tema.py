import tkinter as tk

BG = "#0F0F0F"
CARD = "#1A1A1A"
ORANGE = "#FF7A00"
ORANGE_DARK = "#CC6200"
TEXT = "#F5F5F5"
MUTED = "#B8B8B8"
ERROR = "#FF4D4D"
SUCCESS = "#3DDC84"

FONT_TITLE = ("Arial", 20, "bold")
FONT_SUBTITLE = ("Arial", 13, "bold")
FONT_NORMAL = ("Arial", 11)
FONT_BUTTON = ("Arial", 11, "bold")


def clear_frame(frame):
    frame.configure(bg=BG)


def title(parent, text):
    return tk.Label(
        parent,
        text=text,
        bg=BG,
        fg=ORANGE,
        font=FONT_TITLE
    )


def label(parent, text):
    return tk.Label(
        parent,
        text=text,
        bg=BG,
        fg=TEXT,
        font=FONT_NORMAL
    )


def entry(parent, show=None):
    return tk.Entry(
        parent,
        show=show,
        bg="#262626",
        fg=TEXT,
        insertbackground=TEXT,
        relief="flat",
        font=FONT_NORMAL,
        width=30
    )


def button(parent, text, command, secondary=False):
    return tk.Button(
        parent,
        text=text,
        command=command,
        bg=CARD if secondary else ORANGE,
        fg=TEXT,
        activebackground=ORANGE_DARK,
        activeforeground=TEXT,
        relief="flat",
        bd=0,
        font=FONT_BUTTON,
        cursor="hand2",
        width=22,
        pady=8
    )


def card(parent):
    frame = tk.Frame(parent, bg=CARD, padx=30, pady=30)
    return frame