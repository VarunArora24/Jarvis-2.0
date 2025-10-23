from flask import Flask, render_template
from serverless_wsgi import handle_request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# Vercel entry point
def handler(event, context):
    return handle_request(app, event, context)
