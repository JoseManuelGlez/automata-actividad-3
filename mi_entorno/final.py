from flask import Flask, render_template, request
from lark import Lark
from grammar import grammar

app = Flask(__name__)

mensajeERROR = ""
bandera = False
texto = ""

@app.route('/')
def pagina():
    return render_template('formulario.html', bandera='', texto=texto)

@app.route('/procesar_formulario', methods=['POST'])
def procesar_formulario():
    global mensajeERROR, bandera

    texto = request.form.get('texto')

    parser = Lark(grammar, start='start')

    try:
        parser.parse(texto)
        bandera=True
        mensajeERROR=" "
    except Exception as e:
        print("errorsito")
        bandera=False
        mensajeERROR = str(e).split('\n')[0]

    return render_template('formulario.html', bandera=bandera, texto=texto, mensajeERROR=mensajeERROR)

if __name__ == '__main__':
    app.run(debug=True)