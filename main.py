import requests
from bs4 import BeautifulSoup
import base64
import json

TOKEN = "escreva o token aqui"

SCRAPE_URL = "https://intern.aiaxuropenings.com/scrape/6d86a3c6-1982-4df7-9c23-fad25aa6aeb6"
INFERENCIA_URL = "https://intern.aiaxuropenings.com/v1/chat/completions"
SUBMISSAO_URL = "https://intern.aiaxuropenings.com/api/submit-response"

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

def get_image_bytes():
    print("[INFO] Fazendo scraping da página...")
    response = requests.get(SCRAPE_URL)
    if response.status_code != 200:
        raise Exception(f"[ERRO] Falha ao acessar página: {response.status_code}")

    soup = BeautifulSoup(response.text, "html.parser")
    img_tag = soup.find("img")
    if not img_tag or "src" not in img_tag.attrs:
        raise Exception("[ERRO] Tag <img> não encontrada ou sem atributo 'src'.")

    img_data_url = img_tag["src"]
    print(f"[INFO] URL da imagem encontrada (base64): {img_data_url[:30]}...")

    if not img_data_url.startswith("data:image/jpeg;base64,"):
        raise Exception("[ERRO] Formato de imagem inesperado. Esperado base64 embutido.")

    b64_data = img_data_url.split(",")[1]  # Remove o prefixo "data:image/jpeg;base64,"
    print("[INFO] Imagem extraída com sucesso.")
    return base64.b64decode(b64_data)  # Converte para bytes

def send_image_to_model(image_bytes):
    print("[INFO] Enviando imagem ao modelo de IA...")
    b64_image = base64.b64encode(image_bytes).decode("utf-8")

    payload = {
        "model": "microsoft-florence-2-large",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{b64_image}"
                        }
                    },
                    {
                        "type": "text",
                        "text": "<DETAILED_CAPTION>"
                    }
                ]
            }
        ]
    }

    response = requests.post(INFERENCIA_URL, headers=HEADERS, json=payload)
    if response.status_code != 200:
        print(f"[ERRO] Falha na chamada da API. Status: {response.status_code}. Resposta: {response.text}")
        raise Exception("Erro ao enviar imagem ao modelo.")

    print("[INFO] Resposta do modelo recebida.")
    return response.json()

def submit_response(response_json):
    print("[INFO] Submetendo a resposta...")
    response = requests.post(SUBMISSAO_URL, headers=HEADERS, json=response_json)
    if response.status_code == 200:
        print("[✅] Resposta submetida com sucesso!")
        print("👉 Pressione F5 na plataforma para visualizar.")
    else:
        print(f"[ERRO] Falha na submissão. Status: {response.status_code}. Resposta: {response.text}")
        raise Exception("Erro na submissão.")

if __name__ == "__main__":
    print("--- Iniciando o desafio de avaliação técnica ---")
    try:
        img_bytes = get_image_bytes()
        model_response = send_image_to_model(img_bytes)
        submit_response(model_response)
    except Exception as e:
        print(f"[FALHA CRÍTICA] {e}")
        print("[FALHA] Verifique as mensagens de erro acima e seu TOKEN.")
    print("--- Fim da execução do script ---")
