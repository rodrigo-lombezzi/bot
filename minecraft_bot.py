from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Criando o bot
bot = ChatBot("MinecraftBot")

# Texto para treinar o bot
bot.train([
'Oi',
'Olá!',
'Eu quero fazer uma farm',
'Me diga qual farm que você quer fazer',
'Uma farm de obsidian',
'Para farmar obsidian a melhor maneira de obte-la é no The end, com um beacon com haste II e uma picareta de netherite com eficiencia 5, para minerar todos os pilares do end.',
'Como pegar netherine?',
'No Nether, com uma picareta de diamante com eficiencia 2, vá até a camada 13 para minerar, ou faça várias camas para explodi-las, já que no nether não é possivel dormir.'
'Como fazer uma farm de lã?'
'Primeiro encontre uma ovelha, prenda ela e coloque um observador na grama de baixo dela, depois lique o sinal de redstone em um dispenser para coletar a lã e coloque um carrinho com funil para a coleta.'
])

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
