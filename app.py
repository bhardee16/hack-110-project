from flask import Flask, render_template, request

app: Flask = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/parks", methods=["GET", "POST"])
def parks():
    if request.method == "POST":
        park: str = request.form['park']


        return render_template("result.html", park=park)
    return render_template("parks.html")


if __name__ == '__main__':
    app.run(debug=True)
