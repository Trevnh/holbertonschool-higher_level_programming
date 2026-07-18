"""Module for running basic flask using Jinja"""
from flask import Flask, render_template, request
import json
import csv
import sqlite3


app = Flask(__name__)

def read_json_file(filename):
    """Read product data from JSON file"""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)

def read_csv_file(filename):
    """Read product data from csv file"""
    data = []
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            data.append(row)
        return data
    
def read_sql_database(filename):
    """Read product data from SQLite database"""
    connection = sqlite3.connect(filename)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute(
        "SELECT id, name, category, price from PRODUCTS"
    )

    rows = cursor.fetchall()
    products = [dict(row) for row in rows]

    connection.close()

    return products

@app.route('/products')
def products():
    """Display products from given data sources"""
    source = request.args.get("source")
    product_id = request.args.get("id")
    error = None

    try:
        if source == 'json':
            product_list = read_json_file("products.json")
        elif source == 'csv':
            product_list = read_csv_file("products.csv")
        elif source == 'sql':
            product_list = read_sql_database('products.db')
        else:
            return render_template(
                'product_display.html',
                error='Wrong source',
                products=[]
            )
    except (OSError, json.JSONDecodeError, csv.Error, sqlite3.Error):
        product_list = []
        error = 'Database error'

    if error is None and product_id is not None:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template(
                'product_display.html',
                error='Product not found',
                products=[]
            )
        
        product_list = [
            product for product in product_list
            if product["id"] == product_id
        ]

        if not product_list:
            return render_template(
                'product_display.html',
                error='Product not found',
                products=[]
            )
        
    return render_template(
        'product_display.html',
        error=error,
        products=product_list
    )

if __name__ == '__main__':
    app.run(debug=True, port=5000)
