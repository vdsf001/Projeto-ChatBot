from flask import Flask

app =  Flask(__name__)
@app.route('/')
def index():
    return 'Route is working'


if __name__== "main":
    app.run()






