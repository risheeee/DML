from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task = request.form["task"]
        priority = request.form["priority"]
        tasks.append({"task": task, "priority": priority, "done": False})
        return redirect("/")
    return render_template("index.html", tasks=tasks)

@app.route("/done/<int:id>")
def done(id):
    tasks[id]["done"] = True
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)