from flask import Flask, request

app =  Flask(__name__)
@app.route('/')
def index():
    param = request.args.get("Pergunta")
    return f"Route is working -- {param}"

if __name__== "main":
    app.run()






