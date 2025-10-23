from flask import Flask, render_template
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

@app.route("/")
def home():
    return render_template("index.html")

# Vercel entry point
def handler(environ, start_response):
    from werkzeug.wrappers import Request, Response
    request = Request(environ)
    response = Response(app.full_dispatch_request())
    return response(environ, start_response)
