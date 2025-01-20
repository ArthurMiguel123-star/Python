import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk
import requests

class QRCodeGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerador de QR Code")

        self.label = tk.Label(root, text="Insira o link:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=10)

        self.generate_button = tk.Button(root, text="Gerar QR Code", command=self.generate_qr_code)
        self.generate_button.pack(pady=10)

        self.canvas = tk.Canvas(root, width=300, height=300)
        self.canvas.pack(pady=10)

        self.logo_canvas = tk.Canvas(root, width=100, height=100)
        self.logo_canvas.pack(pady=10)

    def generate_qr_code(self):
        link = self.entry.get()
        if not link:
            messagebox.showwarning("Aviso", "Por favor, insira um link.")
            return

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(link)
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')
        img = img.resize((300, 300), Image.LANCZOS)
        img = ImageTk.PhotoImage(img)

        self.canvas.create_image(150, 150, image=img)
        self.canvas.image = img

        self.check_social_media(link)

    def check_social_media(self, link):
        social_media_logos = {
            "facebook.com": "facebook_logo.png",
            "twitter.com": "twitter_logo.png",
            "instagram.com": "instagram_logo.png",
            "linkedin.com": "linkedin_logo.png",
        }

        for domain, logo in social_media_logos.items():
            if domain in link:
                self.display_logo(logo)
                break

    def display_logo(self, logo_path):
        try:
            logo_img = Image.open(logo_path)
            logo_img = logo_img.resize((100, 100), Image.LANCZOS)
            logo_img = ImageTk.PhotoImage(logo_img)

            self.logo_canvas.create_image(50, 50, image=logo_img)
            self.logo_canvas.image = logo_img
        except FileNotFoundError:
            messagebox.showerror("Erro", f"Logo não encontrado: {logo_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeGenerator(root)
    root.mainloop()
