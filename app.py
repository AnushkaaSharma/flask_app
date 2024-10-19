from flask import Flask, render_template
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)

connection_string = "mongodb+srv://anushkaasharma12:LU42ZZ1xQcPiUETK@cluster0.oglqn.mongodb.net"

client = MongoClient(connection_string)

db = client.shop_db

products_collection = db.products

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products')
def products():
    products_data = list(products_collection.find())  # Fetch all products
    return render_template('products.html', products=products_data)

if __name__ == '__main__':
    app.run(debug=True)

