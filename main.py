from flask import Flask

#inicialização básica do Flask

app = Flask(__name__)

@app.route("/hello") #definindo a rota (endereço)
def hello():
  return "Hi there"

if __name__ == "__main__":
  app.run()

# ao executar o programa, ele retornará o endereço web, que no nesse caso será:
# http://127.0.0.1:5000
