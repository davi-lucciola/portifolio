from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/contato', methods=['GET'])
def contact():
    return render_template('contact.html')

@app.route('/contato', methods=['POST'])
def contact_message():
    remetente = request.form.get('remetente')
    assunto = request.form.get('assunto')
    mensagem = request.form.get('mensagem')

    resposta = f'Obrigado {remetente} por enviar uma mensagem para Davi Lucciola com o assunto {assunto}'
    return render_template('contact.html', mensagem=resposta)


if __name__ == '__main__':
    app.run(debug=True)