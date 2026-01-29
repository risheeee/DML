from flask import Flask, render_template, request

app = Flask(__name__)

notes = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        title = request.form["title"]
        category = request.form["category"]
        notes.append({"title": title, "category": category})
    return render_template("index.html", notes=notes)

if __name__ == "__main__":
    app.run(debug=True)
