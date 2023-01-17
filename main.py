from flask import Flask, request, render_template
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

#inicialização básica do Flask

app = Flask(__name__)

# criação do bot / nome do bot / armazenamento no banco de dados
suporte_bot = ChatBot("Suporte do Hugo", storage_adapter="chatterbot.storage.SQLStorageAdapter")

trainer = ListTrainer(suporte_bot)

#O nosso chatbot vai aprender por meio de uma lista, com a seguinte estrutura:
# lista = [
#    "mensagem do usuário",
#    "chatbot responde",
#    "mensagem do usuário",
#    "chatbot responde",
#     ...
#]

trainer.train([
  "Olá", 
  "Olá, tudo bem? Como posso te ajudar?",
  "Oi", 
  "Oi, tudo bem? Como posso te ajudar?"
])


@app.route("/")
def home():
  return render_template("index.html")

@app.route("/get")
def get_bot_response():
  userText = request.args.get("msg")
  return str(suporte_bot.get_response(userText))

@app.route("/hello") #definindo a rota (endereço)
def hello():
  return "Hello there"

if __name__ == "__main__":
  app.run()

# ao executar o programa, ele retornará o endereço web, que no nesse caso será:
# http://127.0.0.1:5000