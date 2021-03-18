from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(
    __name__,
    static_folder="static",
    static_url_path="/"
)
app.secret_key = "#230dec61-fee8-4ef2-a791-36f9e680c9fc"


# signin


@app.route("/signin", methods=["POST", "GET"])
def signin():
    if request.method == "POST":
        user = request.form["username"]
        pw = request.form["password"]
        session["user"] = user
        if user == "test" and pw == "test":
            return redirect("/member")
        else:
            return redirect("/error")
    else:
        return redirect("/")


@app.route("/member")
def member():
    if "user" in session:
        user = session["user"]
        return render_template("member.html")
    else:
        return redirect("/")


@app.route("/error")
def error():
    return render_template("error.html")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/signout")
def signout():
    session.pop("user", None)
    return redirect("/")


if __name__ == "__main__":
    app.run(port=3000)
