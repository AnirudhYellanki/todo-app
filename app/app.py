from flask import Flask, request, render_template, redirect

app = Flask(__name__, template_folder="templates")
tasks = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task = request.form.get("task", "").strip()
        if task:
            tasks.append(task)
        return redirect("/")
    return render_template("index.html", tasks=tasks)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
