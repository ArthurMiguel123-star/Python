import tkinter as tk
from tkinter import colorchooser

def choose_color():
    color_code = colorchooser.askcolor(title="Escolha uma cor")
    if color_code:
        color_label.config(text=f"Cor escolhida: {color_code[1]}", bg=color_code[1])
        copy_button.config(state=tk.NORMAL)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(color_label.cget("text").split(": ")[1])
    root.update()  # Mantém a área de transferência atualizada
    copy_label.config(text="Código RGB copiado!")

root = tk.Tk()
root.title("Seletor de Cores")

choose_color_button = tk.Button(root, text="Escolher Cor", command=choose_color)
choose_color_button.pack(pady=20)

color_label = tk.Label(root, text="Cor escolhida: Nenhuma", width=30, height=2)
color_label.pack(pady=20)

copy_button = tk.Button(root, text="Copiar Código RGB", command=copy_to_clipboard, state=tk.DISABLED)
copy_button.pack(pady=20)

copy_label = tk.Label(root, text="", width=30, height=2)
copy_label.pack(pady=20)

root.mainloop()
