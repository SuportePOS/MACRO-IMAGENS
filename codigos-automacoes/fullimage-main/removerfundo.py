import os
import requests
from concurrent.futures import ThreadPoolExecutor
from plyer import notification

nome_da_pasta = 'Imagens'
diretorio_area_de_trabalho = os.path.join(os.path.expanduser('~'), 'Desktop')
caminho_pasta = os.path.join(diretorio_area_de_trabalho, nome_da_pasta)

def remove_background_with_removebg(input_folder, output_folder, api_key):
    # Certifique-se de que a pasta de saída existe, se não, crie-a
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # URL da API Remove.bg
    api_url = "https://api.remove.bg/v1.0/removebg"

    # Lista para armazenar os resultados das solicitações
    results = []

    # Percorre todos os arquivos na pasta de entrada
    for filename in os.listdir(input_folder):
        if filename.endswith(('.jpg', '.jpeg', '.png')):  # Filtra apenas arquivos de imagem
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            # Adiciona o arquivo à lista de resultados
            results.append((input_path, output_path))

    # Função para enviar solicitação para remover o fundo
    def process_image(input_path, output_path):
        with open(input_path, 'rb') as file:
            response = requests.post(api_url,
                                     files={'image_file': file},
                                     data={'size': 'auto'},
                                     headers={'X-Api-Key': api_key})

            # Verifica se a solicitação foi bem-sucedida
            if response.status_code == 200:
                # Salva a imagem processada
                with open(output_path, "wb") as output_file:
                    output_file.write(response.content)
                print(f'{input_path} processado com sucesso!')
                # Notificação de conclusão
                notification.notify(
                    title='Remoção de Fundo Concluída',
                    message=f"As imagens teve seus fundos removido com sucesso!",
                    app_name='Removedor de Fundo',
                )
            else:
                print(f'Erro ao processar {input_path}: {response.text}')

    # Use ThreadPoolExecutor para enviar solicitações em paralelo
    with ThreadPoolExecutor() as executor:
        for input_path, output_path in results:
            executor.submit(process_image, input_path, output_path)

# Pasta de entrada contendo as imagens com fundo
input_folder = caminho_pasta
# Pasta de saída onde as imagens sem fundo serão salvas
output_folder = caminho_pasta
# Sua chave de API Remove.bg
api_key = 'wJSvEEShPrbeGFygtEaJTgvf'

remove_background_with_removebg(input_folder, output_folder, api_key)
