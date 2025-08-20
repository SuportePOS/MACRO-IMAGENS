from PIL import Image, UnidentifiedImageError
from plyer import notification
import os

nome_da_pasta = 'Imagens'
diretorio_area_de_trabalho = os.path.join(os.path.expanduser('~'), 'Desktop')
caminho_pasta = os.path.join(diretorio_area_de_trabalho, nome_da_pasta)

def resize_images(input_folder, target_size=(70, 70)):
    # Lista os arquivos no diretório de entrada
    files = os.listdir(input_folder)

    for file in files:
        # Verifica se o arquivo é uma imagem
        if file.endswith(('.png', '.jpg', '.jpeg', '.gif')):
            # Tenta abrir a imagem
            try:
                # Abre a imagem
                image_path = os.path.join(input_folder, file)
                img = Image.open(image_path)
                
                # Converte a imagem para o modo RGB se estiver no modo RGBA
                if img.mode == 'RGBA':
                    img = img.convert('RGB')

                # Cria uma cópia da imagem original
                img_copy = img.copy()

                # Redimensiona a cópia da imagem
                img_resized = img_copy.resize(target_size)
                
                # Fecha a imagem original
                img.close()

                # Remove a extensão do arquivo
                filename, file_extension = os.path.splitext(file)

                # Define o novo nome de arquivo
                new_filename = f"{filename}.png"

                # Salva a imagem redimensionada como PNG
                output_path = os.path.join(input_folder, new_filename)
                img_resized.save(output_path, "PNG")
                
                # Remove o arquivo original se ele existir
                if os.path.exists(image_path):
                    os.remove(image_path)

                print(f"Imagem {file} redimensionada e substituída por {new_filename}")
                # Notificação de conclusão
                notification.notify(
                    title='Redimensionamento Concluído',
                    message=f"As imagens  foi redimensionada com sucesso!",
                    app_name='Redimensionador de Imagens',
                )
            
            # Trata exceção se não conseguir abrir a imagem
            except UnidentifiedImageError:
                print(f"Erro ao abrir a imagem {file}. O arquivo pode estar corrompido ou em um formato não suportado.")

# Pasta de entrada e saída
input_folder = caminho_pasta
# Tamanho desejado
target_size = (70, 70)

# Redimensiona as imagens
resize_images(input_folder, target_size)
