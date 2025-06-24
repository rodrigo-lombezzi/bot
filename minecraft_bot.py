from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

# Criar e treinar bot local com conversas.txt
bot = ChatBot("MinecraftBot")
trainer = ListTrainer(bot)

# Caminho do arquivo
caminho_txt = os.path.join(os.path.dirname(__file__), "conversas.txt")

# Ler e treinar com as perguntas/respostas locais
with open(caminho_txt, "r", encoding="utf-8") as arquivo:
    linhas = [linha.strip() for linha in arquivo if linha.strip()]
    trainer.train(linhas)

# Loop de conversa
print("MinecraftBot pronto! (Digite 'sair' para encerrar)")

while True:
    pergunta = input("Você: ")
    if pergunta.lower() in ["sair", "tchau"]:
        print("MinecraftBot: Até logo!")
        break

    resposta = bot.get_response(pergunta)
    texto_resposta = str(resposta)

    # Verifica se o bot respondeu com confiança
    if float(resposta.confidence) < 0.7 or "não sei" in texto_resposta.lower() or len(texto_resposta) < 10:
        print("MinecraftBot:Não sei isso ainda...")
    else:
        print(f"MinecraftBot: {resposta}")

