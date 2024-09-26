from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])

def homepage():
    if request.method == 'GET':
        return render_template('index.html')
    
    