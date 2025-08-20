import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton
from plyer import notification  # Importar a biblioteca plyer para notificação

nome_da_pasta = 'Imagens'
diretorio_area_de_trabalho = os.path.join(os.path.expanduser('~'), 'Desktop')
caminho_pasta = os.path.join(diretorio_area_de_trabalho, nome_da_pasta)


if not os.path.exists(caminho_pasta):
    os.makedirs(caminho_pasta)
    print("Pasta criada com sucesso na área de trabalho!")
else:
    print("A pasta já existe na área de trabalho.")

def baixar_imagens(nomes_produtos):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)

    contador = 0  # Inicializa o contador

    for nome_produto in nomes_produtos:
        produto = nome_produto.strip().lower()

        # Construir a URL de pesquisa com prefixo para imagens
        search_url = f"https://www.google.com/search?q={produto}&tbm=isch"
        
        # Navegar para a página de pesquisa de imagens
        driver.get(search_url)
        time.sleep(2)

        try:
            contador += 1  # Incrementa o contador

            # Formata o número do contador com dois dígitos
            numero_formatado = str(contador).zfill(2)

            # Cria o nome do arquivo com o número formatado
            nome_arquivo = f"{numero_formatado}.jpg"

            # Encontra a primeira imagem
            first_image = driver.find_element(By.CLASS_NAME, "ob5Hkd")

            # Caminho completo do arquivo
            screenshot_path = os.path.join(caminho_pasta, nome_arquivo)

            # Salva a imagem
            first_image.screenshot(screenshot_path)

        except Exception as e:
            print(f"Erro ao clicar na imagem {contador}: {e}")
            continue

    driver.quit()
    # Após baixar todas as imagens, enviar notificação e fechar a janela
    notification.notify(
        title='Download Concluído',
        message='As imagens foram baixadas com sucesso!',
        app_name='Baixador de Imagens',
    )
    app.quit()  # Fechar a aplicação PyQt5

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Baixar Imagens")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.text_edit = QTextEdit()
        layout.addWidget(self.text_edit)

        self.button = QPushButton("Baixar Imagens")
        self.button.clicked.connect(self.on_button_clicked)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def on_button_clicked(self):
        nomes_produtos = self.text_edit.toPlainText().strip().split("\n")
        baixar_imagens(nomes_produtos)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
