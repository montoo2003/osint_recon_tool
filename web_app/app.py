from flask import Flask, render_template, request
from darkweb_search import darkweb_lookup

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        query = request.form["query"]
        result = darkweb_lookup(query)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
