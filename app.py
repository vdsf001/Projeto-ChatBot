import os
from flask import Flask, request, jsonify
from Textos import lista, respostas
from Bot import Bot
from flask_cors import CORS, cross_origin

app =  Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/question')
@cross_origin()
def index():
    param = request.args.get("pergunta")
    bot = Bot(lista, respostas)

    return jsonify({
        "resposta": bot.find_word(param)
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)






