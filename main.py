from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', resultado='')

@app.route('/fatorial', methods=['POST'])
def fatorial():
    numero = int(request.form['numero'])
    fatorial = 1
    contador = 1

    while contador <= numero:
        fatorial *= contador
        contador += 1

    resultado = fatorial

    return render_template('index.html', resultado=f'O fatorial é {resultado}')

if __name__ == ("__main__"):
    app.run(debug=True)