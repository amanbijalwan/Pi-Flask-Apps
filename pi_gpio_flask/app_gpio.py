from flask import Flask, render_template, redirect, url_for
from gpiozero import LED

app = Flask(__name__)
led = LED(17)
led_state = False

@app.route("/")
def index():
    return render_template("index.html", led_state=led_state)

@app.route("/toggle")
def toggle_led():
    global led_state
    if led_state:
        led.off()
    else:
        led.on()
    led_state = not led_state
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
