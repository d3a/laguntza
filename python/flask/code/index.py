from flask import Flask
from flask import render_template, send_file, request, make_response, url_for, redirect

app = Flask(__name__)

@route("/")
def inicio():
    return render_template('index.html', variable=variable)

@route("/imagen")
def imagen():
    return send_file(path, mime)

@route("/ruta/<param>")
def imagen(param):
    return send_file(path, mime)



if __name__ == "_main_":
    app.run()
