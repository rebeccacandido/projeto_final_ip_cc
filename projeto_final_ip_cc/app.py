from flask import Flask, render_template

app = Flask(__name__) #inicia o Flask dentro da variavel

@app.route('/')
def ola():
   # return '<h1>Olá, Mundo!</h1>'
    return render_template('index.html')

@app.route('/sobre-equipe')
def sobreequipe():
    return render_template('sobre-equipe.html')
app.run()

