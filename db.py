from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["poc_db"]

products = db.products
customers = db.customers
customer_prices = db.customer_prices
