from flask import Flask

from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://mongodb:27017/")

db = client.test_database

collection = db.test_collection

@app.route("/")
def index():
    collection.insert_one({"test" : 1})
    data = collection.find_one()

    with open('text.txt', 'r') as file:
        content = file.read()
    
    display = str(data) + content
    return display
    

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")