from flask import Flask, render_template, request, redirect, url_for
import json, os

app = Flask(__name__)
DATA_FILE = "notes.json"

def load_notes():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE) as f:
            return json.load(f)
    return []

def save_notes(notes):
    with open(DATA_FILE, "w") as f:
        json.dump(notes, f, indent=4)

@app.route("/")
def index():
    notes = load_notes()
    categories = sorted(set(note["category"] for note in notes))
    return render_template("index.html", notes=notes, categories=categories)

@app.route("/add", methods=["POST"])
def add_note():
    notes = load_notes()
    new_note = {
        "title": request.form["title"],
        "category": request.form["category"],
        "done": False
    }
    notes.append(new_note)
    save_notes(notes)
    return redirect(url_for("index"))

@app.route("/toggle/<int:note_id>")
def toggle(note_id):
    notes = load_notes()
    notes[note_id]["done"] = not notes[note_id]["done"]
    save_notes(notes)
    return redirect(url_for("index"))

@app.route("/delete/<int:note_id>")
def delete(note_id):
    notes = load_notes()
    notes.pop(note_id)
    save_notes(notes)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5004, debug=True)
