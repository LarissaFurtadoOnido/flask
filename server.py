from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def homepage():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        name = request.form["name"]
        with open('ListaConvidados.txt', 'a') as arq:
            arq.writelines(name + "\n")
        return render_template('confirmado.html', name=name)


if __name__ == "__main__":
    app.run(debug=True)