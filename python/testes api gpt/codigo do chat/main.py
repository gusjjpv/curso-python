import openai
import time

# Definindo a chave da API
openai.api_key = "api key"

# Função para fazer a requisição com tratamento de erros e controle de taxa
def fazer_requisicao():
    while True:
        try:
            resposta = openai.ChatCompletion.create(
                model='gpt-3.5-turbo',
                messages=[{'role': 'user', 'content': 'O que é uma maçã em até 5 palavras?'}],
                max_tokens=50,  # Redução do número máximo de tokens
                temperature=0,
            )
            return resposta
        except openai.error.RateLimitError:
            print("Limite de requisições atingido. Aguardando para tentar novamente...")
            time.sleep(10)  # Aguarda 10 segundos antes de tentar novamente
        except openai.error.OpenAIError as e:
            print(f"Ocorreu um erro: {e}")
            break

# Faz a requisição e imprime a resposta se bem-sucedida
resposta = fazer_requisicao()
if resposta:
    mensagem_resp = resposta.choices[0].message['content']
    print(mensagem_resp)
