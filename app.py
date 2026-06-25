from flask import Flask, flash, redirect, render_template_string, request, url_for

app = Flask(__name__)
app.secret_key = "secret"

gifts = []

@app.route("/", methods=["GET", "POST"])
def index():
    search_query = request.args.get("search_query")
    search_result = None

    if request.method == "POST":
        gift_name = request.form.get("gift_name", "").strip()
        if not gift_name:
            flash("Порожній подарунок не можна додати!")
        else:
            gifts.append(gift_name)
            flash("Подарунок додано!")
        return redirect(url_for("index"))

    if search_query is not None:
        search_query = search_query.strip()
        if search_query in gifts:
            search_result = "Такий подарунок вже є у списку"
        else:
            search_result = "Такого подарунка ще немає у списку"

    with open("templates/gifts.html", "r", encoding="utf-8") as f:
        html = f.read()

    return render_template_string(html, gifts=gifts, search_result=search_result)

if __name__ == "__main__":
    app.run(debug=True)






