from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def homepage():
    if request.method == 'GET':
        return "render_template('index.html')"


@app.route("/convidados", methods = ['POST'])
def convidados():
    




 if __name__ == "__main__":
    app.run(debug=True)