from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def menu():
    return render_template("menu/menu.html")

@app.route("/middle")
def middle():
    return render_template("middle/middle.html")

@app.route("/roulette")
def roulette():
    return render_template("roulette/roulette.html")

if __name__ == "__main__":
    app.run(debug=True)


