from flask import Flask, render_template
from data import users, nazev_webu, titulek_webu, popis, technologie
from generator import generate_number
app = Flask (__name__)

@app.route("/")
def home():
    titulek_webu = ("Portfolio od Marsiny")
    nazev_webu = ("Samovo portfolio")
    popis = ("Ukázka projektů, výuka s AI, a testování JItsi2")
    technologie = ("Flask", "Python", "HTML", "CSS", "Jitsi2", "Copilot", "Javascript", "C#") 

@app.route("/generator")
def generator():
    return render_template("generator.htm", generate_number=generate_number) 

if __name__ == "__main__":
    app.run(debug=True)
