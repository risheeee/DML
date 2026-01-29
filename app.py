from flask import Flask, render_template, request, redirect

app = Flask(__name__)

notes = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        note = request.form["note"]
        notes.append({"text": note, "done": False})
        return redirect("/")
    return render_template("index.html", notes=notes)

@app.route("/done/<int:id>")
def done(id):
    notes[id]["done"] = not notes[id]["done"]
    return redirect("/")

@app.route("/delete/<int:id>")
def delete(id):
    notes.pop(id)
    return redirect("/")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/stats")
def stats():
    total = len(notes)
    completed = len([n for n in notes if n["done"]])
    return render_template("stats.html", total=total, completed=completed)

if __name__ == "__main__":
    app.run(debug=True)
