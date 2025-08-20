import tkinter as tk
import subprocess

from tkinter import messagebox
import requests
from PIL import Image, ImageTk
from io import BytesIO
import os


def baixarimagens():
       subprocess.run(["python", "baixarimg.py"])

def redimensionar():
       subprocess.run(["python", "redimensionar.py"])

def remover_fundo():
     subprocess.run(["python", "removerfundo.py"])

def get_logo_image(url, size):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img = img.resize(size)
    return ImageTk.PhotoImage(img)

def download_icon(url):
    response = requests.get(url)
    icon = Image.open(BytesIO(response.content))
    return icon

def save_icon(icon, filename):
    icon.save(filename)

def set_window_icon(root, icon_path):
    root.iconbitmap(icon_path)

def set_taskbar_icon(root, icon_path):
    root.iconbitmap(default=icon_path)

def on_enter_scale(event):
    event.widget.config(bg="#6495ED", fg="white")

def on_leave_scale(event):
    event.widget.config(bg="white", fg="#0c2846")

def main():
    # URL do ícone
    icon_url = "https://i.postimg.cc/BnscFS42/Sem-nome-1080-x-900-px.png"

    # Baixar o ícone
    icon = download_icon(icon_url)

    # Salvar o ícone como um arquivo temporário
    temp_icon_path = "temp_icon.ico"
    save_icon(icon, temp_icon_path)

    # Criar a janela principal
    root = tk.Tk()
    root.title("FullImage")
    root.geometry("500x800")
    root.configure(bg="#0c2846")
    root.resizable(False, False)

    # Definir o ícone da janela e da barra de tarefas
    set_window_icon(root, temp_icon_path)
    set_taskbar_icon(root, temp_icon_path)

    container = tk.Frame(root, bg="#0c2846")
    container.pack(expand=True, padx=20, pady=20)

    logo_frame = tk.Frame(container, bg="#0c2846")
    logo_frame.pack(pady=(0, 50))

    logo_url = "https://i.postimg.cc/BnscFS42/Sem-nome-1080-x-900-px.png"
    logo_image = get_logo_image(logo_url, (250, 200))  # Defina o tamanho desejado da logo aqui
    logo_label = tk.Label(logo_frame, image=logo_image, bg="#0c2846")
    logo_label.pack()

    title_label = tk.Label(logo_frame, text="FullImage", font=("Arial", 24), fg="white", bg="#0c2846")
    title_label.pack(pady=(10, 0))

    buttons_frame = tk.Frame(container, bg="#0c2846")
    buttons_frame.pack()

    button_params = {"font": ("Arial", 16), "bg": "white", "fg": "#0c2846", "width": 20}

    baixar_button = tk.Button(buttons_frame, text="Baixar Imagens", command=baixarimagens, **button_params)
    baixar_button.pack(pady=10)
    baixar_button.bind("<Enter>", on_enter_scale)
    baixar_button.bind("<Leave>", on_leave_scale)

    redimensionar_button = tk.Button(buttons_frame, text="Redimensionar", command=redimensionar, **button_params)
    redimensionar_button.pack(pady=10)
    redimensionar_button.bind("<Enter>", on_enter_scale)
    redimensionar_button.bind("<Leave>", on_leave_scale)

    remover_fundo_button = tk.Button(buttons_frame, text="Remover Fundo", command=remover_fundo, **button_params)
    remover_fundo_button.pack(pady=10)
    remover_fundo_button.bind("<Enter>", on_enter_scale)
    remover_fundo_button.bind("<Leave>", on_leave_scale)

    footer_label = tk.Label(container, text="Todos os direitos reservados\n© 2024 FullImage, by Arlei Dev",
                            font=("Arial", 12), fg="white", bg="#0c2846")
    footer_label.pack(pady=50)

    root.mainloop()

    # Remover o arquivo temporário do ícone após fechar a janela
    os.remove(temp_icon_path)

if __name__ == "__main__":
    main()
