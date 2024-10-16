from senha import API_KEY
import requests
import json

"""
exemplo de requisicao(requisicao para ver os modelos)
headers = {"Authorization": f"Bearer {API_KEY}"}
link = "https://api.openai.com/v1/models"
requisicao = requests.get(link, headers=headers)

print(requisicao)
print(requisicao.text)

"""

headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
link = "https://api.openai.com/v1/chat/completions"
id_model = "gpt-3.5-turbo"

body_messagem = {
    "model":id_model,
    "messages":[{"role": "user", "content": "escreva uma mensagem de bom dia para o grupo da familia"}]
}

body_messagem = json.dumps(body_messagem)

requisicao = requests.post(link, headers=headers, data=body_messagem)

print(requisicao)
print(requisicao.text)

resposta = requisicao.json()
mensagem = resposta["choices"][0]["message"]["content"]
print(mensagem)
