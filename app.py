from flask import Flask, render_template

app = Flask(__name__)
# app.config["PORT"] = 5001


@app.route("/")
def index():
    return render_template("index.html"), 200


@app.route("/login")
def login():
    return render_template("login.html"), 200


@app.route("/register")
def register():
    return render_template("register.html"), 200


if __name__ == "__main__":
    app.run(port=5001)
