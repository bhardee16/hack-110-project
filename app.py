from typing import Union
from flask import Flask, render_template, request
from requests import get
from api import get_park_activities

app: Flask = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/parks", methods=["GET", "POST"])
def parks():
    if request.method == "POST":
        park: str = request.form['parks']
        data: dict[str, str] = get_park_activities(park)
        data_dict: dict[str, str] = data["data"][0]
        activities: list[dict[str, str]] = data_dict["activities"]
        return render_template("result.html", park=park, data=activities)
    
    return render_template("parks.html")


# @app.route("/result", methods=["GET", "POST"])
# def result():
#     if request.method == "POST":
#         data: dict[str, str] = get_park_activities
#         return render_template("result.html", data=data)
#     return render_template("result.html")



if __name__ == '__main__':
    app.run(debug=True)
