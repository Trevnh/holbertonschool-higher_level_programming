"""Module for running basic flask using Jinja"""
from flask import Flask, render_template, request
import json
import csv


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

@app.route('/products')
def products():
    """Display products from given data sources"""
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        product_list = read_json_file("products.json")
    elif source == 'csv':
        product_list = read_csv_file("products.csv")
    else:
        return render_template(
            'product_display.html',
            error='Wrong source',
            products=[]
        )
    
    if product_id is not None:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template(
                'product_display.html',
                error='Product not found',
                products=[]
            )

        if not product_list:
            return render_template(
                'product_display.html',
                error='Product not found',
                products=[]
            )
        
    return render_template(
        'product_display.html',
        error=None,
        products=product_list
    )

if __name__ == '__main__':
    app.run(debug=True, port=5000)