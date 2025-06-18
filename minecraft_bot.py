from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Criando o bot
bot = ChatBot("MinecraftBot")

# Lendo o arquivo de texto com perguntas e respostas
with open("conversas.txt", "r", encoding="utf-8") as arquivo:
    linhas = [linha.strip() for linha in arquivo if linha.strip()]

# Treinando o bot com as linhas do arquivo
trainer = ListTrainer(bot)
trainer.train(linhas)

# Loop de conversa
print("MinecraftBot pronto! (Digite 'sair' para encerrar)")
while True:
    pergunta = input("Você: ")
    if pergunta.lower() in ["sair", "tchau"]:
        print("MinecraftBot: Até logo!")
        break
    resposta = bot.get_response(pergunta)
    print(f"MinecraftBot: {resposta}")
