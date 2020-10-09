from flask import Flask, request, jsonify

app =  Flask(__name__)
@app.route('/question')
def index():
    param = request.args.get("pergunta")
    return jsonify({
        "resposta": "Testando"
    })

if __name__== "main":
    app.run()






