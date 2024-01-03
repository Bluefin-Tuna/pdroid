"""File for defining application and serving of templates using Flask."""

from flask import Flask, render_template, request
from lib import generate_ticket

app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html"), 200

@app.post("/ticket")
def create_ticket():
    title = request.form.get("title", type=str)
    ticket = {"ticket": str(generate_ticket(title))}
    return render_template("ticket.html", ticket=ticket), 201

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True)