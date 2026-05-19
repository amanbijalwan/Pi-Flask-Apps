from flask import Flask, render_template, request, jsonify
import json, random

app = Flask(__name__)

with open("quotes.json") as f:
    quotes = json.load(f)

@app.route("/")
def index():
    categories = list(quotes.keys())
    return render_template("index.html", categories=categories)

@app.route("/get_quote", methods=["POST"])
def get_quote():
    category = request.form.get("category")
    if category in quotes:
        quote = random.choice(quotes[category])
        return jsonify({"quote": quote})
    return jsonify({"quote": "No quotes found for this category."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003, debug=True)
