import tkinter as tk

class DrawApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicativo de Desenho")

        self.canvas = tk.Canvas(self.root, bg="white", width=800, height=600)
        self.canvas.pack()

        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

        self.old_x = None
        self.old_y = None

        self.color = "black"
        self.setup_buttons()

    def setup_buttons(self):
        button_frame = tk.Frame(self.root)
        button_frame.pack(side=tk.TOP, fill=tk.X)

        colors = ["black", "red", "green", "blue", "yellow", "purple", "orange"]
        for color in colors:
            button = tk.Button(button_frame, bg=color, width=2, command=lambda c=color: self.change_color(c))
            button.pack(side=tk.LEFT)

        clear_button = tk.Button(button_frame, text="Limpar", command=self.clear_canvas)
        clear_button.pack(side=tk.LEFT)

        eraser_button = tk.Button(button_frame, text="Borracha", command=self.use_eraser)
        eraser_button.pack(side=tk.LEFT)

    def change_color(self, new_color):
        self.color = new_color

    def clear_canvas(self):
        self.canvas.delete("all")

    def use_eraser(self):
        self.color = "white"

    def paint(self, event):
        if self.old_x and self.old_y:
            self.canvas.create_line(self.old_x, self.old_y, event.x, event.y, width=5, fill=self.color, capstyle=tk.ROUND, smooth=tk.TRUE)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x = None
        self.old_y = None

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawApp(root)
    root.mainloop()
