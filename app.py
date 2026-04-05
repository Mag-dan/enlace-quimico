import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_ENV") != "production"
    print(f"Servidor corriendo en http://localhost:{port}")
    app.run(host="0.0.0.0", port=port, debug=debug)
