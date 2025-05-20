#!/usr/bin/env python3

from flask import Flask, render_template
from livereload import Server

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True  # Ensure templates are auto-reloaded

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    server = Server(app.wsgi_app)
    server.watch('templates/*.html')  # Watch all HTML templates
    server.watch('app.py')  # Auto-restart when Python code changes
    server.serve(debug=True, port=5500)  # Or 5000 if you prefer
