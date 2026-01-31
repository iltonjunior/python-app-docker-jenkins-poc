from flask import Flask, render_template
import socket
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        "index.html",
        hostname=socket.gethostname(),
        now=datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
