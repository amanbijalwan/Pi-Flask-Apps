from flask import Flask, render_template
import psutil, datetime

app = Flask(__name__)

@app.route("/")

def dashboard():
    stats = {
        "cpu_percent": psutil.cpu_percent(interval=1),
        "mem_percent": psutil.virtual_memory().percent,
        "disk_percent": psutil.disk_usage("/").percent,
        "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return render_template("index.html", stats=stats)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
