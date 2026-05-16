from flask import Flask, render_template
import psutil, datetime, os

app = Flask(__name__)

def get_uptime():
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    return str(datetime.datetime.now() - boot_time).split('.')[0]  # hh:mm:ss

@app.route("/")
def dashboard():
    stats = {
        "cpu_percent": psutil.cpu_percent(interval=1),
        "mem_percent": psutil.virtual_memory().percent,
        "disk_percent": psutil.disk_usage("/").percent,
        "net_sent": round(psutil.net_io_counters().bytes_sent / (1024*1024), 2),
        "net_recv": round(psutil.net_io_counters().bytes_recv / (1024*1024), 2),
        "uptime": get_uptime(),
        "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "cpu_count": psutil.cpu_count(logical=True)
    }
    return render_template("index.html", stats=stats)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
