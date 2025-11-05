from flask import Flask, render_template, request
from data import users, nazev_webu, titulek_webu, popis, technologie
from generator import generate_number
app = Flask (__name__)

products = {
    1: {"name": "Notebook", "price": 25000},
    2: {"name": "Myš", "price": 500},
    3: {"name": "Klávesnice", "price": 1000},
}

@app.route("/", methods=["GET"])
def search():
    q = request.args.get("q", "").strip()
    result = None

    if q:
        if q.isdigit() and int(q) in products:
            result = {int(q): products[int(q)]}
        else:
            for pid, data in products.items():
                if data["name"].lower() == q.lower():
                    result = {pid: data}
                    break
            if not result:
                for pid, data in products.items():
                    if q.lower() in data["name"].lower():
                        result = {pid: data}
                        break

    return render_template("eshop.html", products=result, q=q)


@app.route("/add", methods=["POST"])
def add_product():
    name = request.form.get("name")
    price = request.form.get("price")

    if name and price:
        new_id = max(products.keys(), default=0) + 1
        products[new_id] = {"name": name, "price": float(price)}

    return redirect(url_for("search"))

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
