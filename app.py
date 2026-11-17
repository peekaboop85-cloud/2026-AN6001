from math import isfinite

import joblib
from flask import Flask, render_template, request
dbsModel = joblib.load("DBS_SGD_model.pkl")

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return render_template("index.html")

@app.route("/main",methods=["GET","POST"])
def main():
    q = request.form.get("q")
    return render_template("main.html") 

@app.route("/dbs",methods=["GET","POST"])
def dbs():

    return render_template("dbs.html") 
@app.route("/dbsP",methods=["GET","POST"])
def dbsP():
    if request.method == "GET":
        return dbs()

    q = request.form.get("q", type=float)
    if q is None or not isfinite(q):
        return render_template("dbs.html", error="Enter a valid exchange rate."), 400

    r = dbsModel.predict([[q]])
    return render_template("dbs.html", r=r[0][0]) 

if __name__ == "__main__":
     app.run(debug=True)


