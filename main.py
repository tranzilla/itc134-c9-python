#render_template looks for templates folder(HTML File)
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/history")
def history():
	return render_template("history.html")

@app.route("/game")
def game():
	return render_template("app.html")

if __name__ == "__main__":
    app.run(debug=True)