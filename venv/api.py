from flask import Flask, render_template, redirect, url_for, request
from classes import Website

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
    print("refresh page")
    if request.method == "POST":
        try:
            name = request.form['input_name']
            id = request.form['input_id']
            url = request.form['input_url']
            website = Website(name, id, url)
        except ValueError:
            print("Cannot created")
    return render_template("websites.html", websites= Website.websites)


@app.route("/websites/remove", methods=["GET", "POST"])
def remove():
    print("try to remove")
    if request.method == "POST":
        obj = request.form['obj']
        print(dir(obj))
        Website.websites.remove(obj)
    return render_template("websites.html", websites= Website.websites)


#app.run(debug=True, host='0.0.0.0', port=80)