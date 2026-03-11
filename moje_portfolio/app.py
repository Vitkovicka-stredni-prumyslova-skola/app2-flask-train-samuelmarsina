from flask import  Flask, render_template, request
from data import *
from generator import generate_number

app = Flask (__name__)


@app.route("/", methods=["GET","POST"])
def home():
    email = None
    nickSamuel = "samuel" 
    hesloSamuel = "tajneheslo"  
    zpravaLogin = None

    if request.method == "GET":
        email = request.args.get("email")
    
    if request.method == "POST":
        nick = request.form.get("nick")
        heslo = request.form.get("heslo")

        if nick == nickSamuel and heslo == hesloSamuel:
            zpravaLogin = "Přihlášení proběhlo úspěšně!"
        else:
            zpravaLogin = "Špatný login nebo heslo"

        

    return render_template("index.htm", nazev_webu = nazev_webu, titulek_webu = titulek_webu, technologie = technologie, email = email, nickRadek = nickRadek, hesloSamuel = hesloSamuel, zpravaLogin = zpravaLogin)

@app.route("/contacts")
def cotnacts():
    return render_template("contacts.htm", users=users)

@app.route("/generator")
def generator():
    return render_template("generator.htm", generate_number=generate_number)

@app.route("/eshop", methods=["GET","POST"])
def eshop():
    q = request.args.get("q") or request.args.get("dotaz") or request.args.get("search") or ""
    q_str = q.strip()
    results = []
    not_found = None
    add_message = None
    add_error = None

    if request.method == "POST" and request.form.get("add_product") is not None:
        nazev = request.form.get("nazev", "").strip()
        popis_f = request.form.get("popis", "").strip()
        cena_f = request.form.get("cena", "").strip()
        mena_f = request.form.get("mena", "CZK").strip() or "CZK"
        skladem_f = request.form.get("skladem", "0").strip()

        
        if not nazev:
            add_error = "Název je povinný."
        else:
            try:
                cena_val = float(cena_f.replace(",", "."))
                skladem_val = int(float(skladem_f))  
                
                max_id = max((p.get("id", 0) for p in produkty), default=0)
                new_id = max_id + 1
                new_product = {
                    "id": new_id,
                    "nazev": nazev,
                    "cena": round(cena_val, 2),
                    "mena": mena_f,
                    "popis": popis_f,
                    "skladem": skladem_val
                }
                produkty.append(new_product)
                add_message = f"Produkt '{nazev}' byl přidán (ID {new_id})."
                
                q_str = ""
            except ValueError:
                add_error = "Neplatná cena nebo počet skladem (použij číslo)."

    
    if not q_str:
        results = produkty
    else:
        qlow = q_str.lower()
        if q_str.isdigit():
            pid = int(q_str)
            by_id = [p for p in produkty if p["id"] == pid]
            if by_id:
                results = by_id

        if not results:
            exact = [p for p in produkty if p["nazev"].lower() == qlow]
            if exact:
                results = exact

        if not results:
            partial_name = [p for p in produkty if qlow in p["nazev"].lower()]
            partial_desc = [p for p in produkty if qlow in p["popis"].lower() and p not in partial_name]
            if partial_name or partial_desc:
                results = partial_name + partial_desc

        if not results:
            not_found = f"Podle zadaného výrazu '{q_str}' nebylo nic nalezeno."

    return render_template("eshop.htm", produkty=results, q=q_str, not_found=not_found, add_message=add_message, add_error=add_error)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.htm'), 404

@app.route("/javascript")
def scripty():
    return render_template("javascript.htm")

@app.route("/dom")
def javascript():
    return render_template("dom.htm")

@app.route("/todo")
def todo():
    return render_template("todo.htm")

@app.route("/regform")
def regform():
    return render_template("reg-form.htm")

if __name__ == "__main__":
    app.run(debug=True)
