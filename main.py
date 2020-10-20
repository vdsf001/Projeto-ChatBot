from flask import Flask, request, jsonify
from Textos import lista, respostas
from Bot import Bot

app =  Flask(__name__)
@app.route('/question')
def index():
    param = request.args.get("pergunta")
    bot = Bot(lista, respostas)

    return jsonify({
        "resposta": bot.find_word(param)
    })

if __name__== "main":
    app.run()






