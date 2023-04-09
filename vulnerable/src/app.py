from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return """<h1>CVE-2022-29361 | Client-Side Desync to XSS</h1>
    <script src='/static/main.js'></script>"""

if __name__ == "__main__":
    app.run("0.0.0.0", 5001)
