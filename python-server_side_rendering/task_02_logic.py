"""Module for running basic flask using Jinja"""
from flask import Flask, render_template
import json


app = Flask(__name__)

@app.route('/')
def home():
    """Display Homepage"""
    return render_template('index.html')

@app.route('/about')
def about():
    """Display About page"""
    return render_template('about.html')

@app.route('/contact')
def contact():
    """Display Contact page"""
    return render_template('contact.html')

@app.route('/items')
def items():
    """Display Items stored in the JSON File"""
    with open("items.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    return render_template(
        'items.html',
        items=data.get('items',[])
    )

if __name__ == '__main__':
    app.run(debug=True, port=5000)