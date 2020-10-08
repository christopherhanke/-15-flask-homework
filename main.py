from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")


@app.route("/fakebook")
def fakebook():
    return render_template("projects/fakebook.html")


@app.route("/boogle")
def boogle():
    return render_template("projects/boogle.html")


@app.route("/hair")
def hair():
    return render_template("projects/hairsalon.html")


if __name__ == "__main__":
    app.run(debug=True)
