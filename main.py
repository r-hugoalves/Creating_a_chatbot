#importações necessárias
# Para treinar o nosso chatbot, vamos utilzar o "ListTrainer"

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot('Suporte Hugo')

#O nosso chatbot vai aprender por meio de uma lista, com a seguinte estrutura:
# lista = [
#    "mensagem do usuário",
#    "chatbot responde",
#    "mensagem do usuário",
#    "chatbot responde",
#     ...
#]

conversa = ["Oi", "Oi, tudo bem? Como posso te ajudar?", "Bom dia", "Bom dia, tudo bem? Como posso te ajudar?",
            "Boa noite", "Boa noite, tudo bem? Como posso te ajudar?"]

trainner = ListTrainer(chatbot)
trainner.train(conversa)

while True:
  mensagem = input('Mande uma mensagem.: ')
  if mensagem == "parar":
    break
  resposta = chatbot.get_response(mensagem)
  print(resposta)