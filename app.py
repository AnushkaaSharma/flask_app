from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

connection_string = "mongodb+srv://anushkaasharma12:iHBe0r2quz4StUeR@cluster0.oglqn.mongodb.net/"

client = MongoClient(connection_string)

db = client.shop_db

products_collection = db.products

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products')
def products():
    products = list(products_collection.find())  
    print(products) 
    return render_template('products.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
