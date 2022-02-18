from flask import Flask,render_template,request,url_for,redirect
app = Flask(__name__)
@app.route("/")
@app.route("/<nombre>")
def home(nombre="invitado"):
    if nombre=="invitado":
        return f"Hola {nombre}<br><a href='/login'>Ir a login</a>"
    else:
        return f"<h2>Hola {nombre}</h2>"

@app.route("/login",methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        name = request.form['login']
        return redirect(url_for('home',nombre=name))
    else:
        return render_template("login.html")