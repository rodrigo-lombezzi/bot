from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Cria ou carrega o bot, usando SQLite para armazenar o conhecimento
bot = ChatBot(
    "MinecraftBot",
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///db.sqlite3'  
)

# Usa o treinador de lista para ensinar o bot em tempo real
trainer = ListTrainer(bot)

print("MinecraftBot pronto! (Digite 'sair' para encerrar)")
name = input("Digite seu nome: ")
print("Olá " + name + ", como posso te ajudar com o Minecraft?")

# Início do loop de conversa
while True:
    request = input("Você: ")  
    if request.lower() in ["sair", "tchau"]:
        print("MinecraftBot: Até logo!") 
        break

    # Pede uma resposta ao bot
    resposta = bot.get_response(request) 

    # Se a confiança da resposta for baixa ou a resposta parecer vaga, pergunta ao usuário
    if float(resposta.confidence) < 0.9 or "não sei" in str(resposta).lower():
        print("MinecraftBot: Não sei isso ainda. Você pode me ensinar?")
        nova_resposta = input("Você: (ensine a resposta correta) ")
        
        # Se o usuário fornecer uma resposta válida, o bot aprende na hora
        if nova_resposta.strip():
            trainer.train([request, nova_resposta])  
            print("MinecraftBot: Obrigado! Agora eu sei.")  
    else:
        print(f"MinecraftBot: {resposta}") 
