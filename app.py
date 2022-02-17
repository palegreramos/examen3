from flask import Flask,render_template,request,url_for,redirect
app = Flask(__name__)
@app.route("/")
@app.route("/<nombre>")
def home(nombre="Pili"):
    return f"Hola {nombre}, Flask!"

@app.route("/login",methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        name = request.form['login']
        return redirect(url_for('home',nombre=name))
    else:
        return render_template("login.html")