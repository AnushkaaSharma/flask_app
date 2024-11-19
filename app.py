from flask import Flask, render_template
from pymongo import MongoClient
import os
from dotenv import load_dotenv
from app import app

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)

# Access environment variables
MONGODB_USERNAME = os.getenv('MONGODB_USERNAME')
MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD')
MONGODB_HOST = os.getenv('MONGODB_HOST')
MONGODB_DB = os.getenv('MONGODB_DB')

connection_string = f"mongodb+srv://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@{MONGODB_HOST}/{MONGODB_DB}?retryWrites=true&w=majority"
client = MongoClient(connection_string)

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

