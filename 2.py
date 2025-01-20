import tkinter as tk


def update_expression(value):
    current_text = display.get()
    display.delete(0, tk.END)
    display.insert(0, current_text + value)


def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(0, "Erro")


def clear_display():
    display.delete(0, tk.END)


def toggle_theme():
    global dark_mode
    if dark_mode:
        root.config(bg="white")
        display.config(bg="white", fg="black")
        for button in buttons_list:
            button.config(bg="lightgray", fg="black")
        theme_button.config(text="Tema Escuro", bg="lightgray", fg="black")
    else:
        root.config(bg="black")
        display.config(bg="black", fg="white")
        for button in buttons_list:
            button.config(bg="gray", fg="white")
        theme_button.config(text="Tema Claro", bg="gray", fg="white")
    dark_mode = not dark_mode


root = tk.Tk()
root.title("Calculadora")


dark_mode = False


display = tk.Entry(root, font=("Arial", 20), borderwidth=2, relief="solid")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


buttons = [
    '7', '8', '9', '/', 
    '4', '5', '6', '*', 
    '1', '2', '3', '-', 
    '0', '.', '=', '+'
]

buttons_list = []
row = 1
col = 0

for button in buttons:
    if button == '=':
        btn = tk.Button(root, text=button, font=("Arial", 20), command=calculate)
    else:
        btn = tk.Button(root, text=button, font=("Arial", 20), command=lambda b=button: update_expression(b))
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    buttons_list.append(btn)
    col += 1
    if col > 3:
        col = 0
        row += 1


clear_button = tk.Button(root, text='C', font=("Arial", 20), command=clear_display)
clear_button.grid(row=row, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")
buttons_list.append(clear_button)


theme_button = tk.Button(root, text="Tema Escuro", font=("Arial", 20), command=toggle_theme)
theme_button.grid(row=row+1, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")


for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(6):
    root.grid_rowconfigure(i, weight=1)


root.mainloop()
