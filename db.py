import os
from pymongo import MongoClient

mongo_uri = os.environ.get("MONGO_URI")
client = MongoClient(mongo_uri)

db = client["pocdb"]


products = db.products
customers = db.customers
customer_prices = db.customer_prices

