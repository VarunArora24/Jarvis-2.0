from flask import Flask, render_template
from http.server import BaseHTTPRequestHandler

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Hello, World!')
