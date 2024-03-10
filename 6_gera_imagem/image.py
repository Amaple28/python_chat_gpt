import openai
import requests

def save_image_from_url(image_url, save_path):
    response = requests.get(image_url)
    response.raise_for_status()  # Verifica se houve algum erro ao fazer a solicitação

    with open(save_path, "wb") as f:
        f.write(response.content)

openai.api_key = "KEY"

prompt = "Leão com espada de cavaleiro"

response = openai.Image.create(
  prompt=prompt,
  n=1, # Quantidade de imagens
  size="1024x1024" # ['256x256', '512x512', '1024x1024']
)

url_image = response.data[0].url

save_image_from_url(url_image, 'imagem.png')