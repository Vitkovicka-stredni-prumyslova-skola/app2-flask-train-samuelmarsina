from flask import Flask, render_template, request
from data import users, nazev_webu, titulek_webu, popis, technologie
from generator import generate_number
app = Flask (__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    email = None
    if request.method == "GET":
        email = request.args.get("email")
        
    return render_template("index.htm", nazev_webu = nazev_webu)

@app.route("/generator")
def generator():
    return render_template("generator.htm", generate_number=generate_number) 

if __name__ == "__main__":
    app.run(debug=True)
