from flask import Flask, redirect, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/home') 

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/sobre-mim')
def about():
    return render_template('sobre-mim.html')


if __name__ == '__main__':
    app.run(debug=True)