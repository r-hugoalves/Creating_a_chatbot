# Creating_a_chatbot
 
O programa tem como objetivo, simular um atendimento (básico) de um suporte de TI

## Pontos importantes e correção de possíveis erros

Para a execução do código, tanto pela web quanto pela máquina é necessáro realizar o seguinte procedimento:

1) Criação de um ambiente virtual

2) pip install chatterbot

Porém, ele estava retornando com o seguinte erro:

"error: command 'C:\\Program Files (x86)\\Microsoft Visual Studio\\2022\\BuildTools\\VC\\Tools\\MSVC\\14.34.31933\\bin\\HostX86\\x64\\cl.exe' failed with exit code 2"

Isso é um erro que de fato pode acontecer durante a instação do chatterbot por meio de um ambiente virtual, mas que pode ser solucionado de maneira simples e eficiente com o seguinte trecho de código:

git clone https://github.com/feignbird/ChatterBot-spacy_fixed.git
pip install ./ChatterBot-spacy_fixed
pip install chatterbot-corpus
pip uninstall pyYAML
pip install pyYAML==5.3.1
python -m spacy download en_core_web_sm

Feito isso, execute novamente o comando e a instação ocorrerá com sucesso!