from flask import Flask, render_template, redirect, url_for, request
from classes import *

app = Flask(__name__)

Website("Bestweather", 1123, "www.bestweather.pt")
Website("Vetcaxias", 25463, "www.vetcaxias.pt")
Website("Huna", 2797, "www.huna.pt")


@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/test")
def hello():
    return "Welcome to my WEB APP!"


@app.route("/websites", methods=["GET", "POST"])
def websites():
    if request.method == "POST":
        try:
            name = request.form['input_name']
            id = request.form['input_id']
            url = request.form['input_url']
            Website(name, id, url)
            return redirect(url_for("websites"))
        except ValueError:
            print("Cannot created")
    return render_template("websites.html", websites= Website.websites)


@app.route("/websites/remove", methods=["GET", "POST"])
def remove():
    if request.method == "POST":
        obj_name = request.form['obj']
        removed = remove_object(obj_name)
        if removed:
            print('website {} removed',format(obj_name))
        else:
            print('Not removed')
    return render_template("websites.html", websites= Website.websites)


#app.run(debug=True, host='0.0.0.0', port=80)