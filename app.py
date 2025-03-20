from flask import Flask, jsonify
from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
env = os.getenv('FLASK_ENV', 'development')
load_dotenv(f'.env.{env}')

app = Flask(__name__)

# Get the MongoDB URI from the environment variable
mongo_uri = os.getenv('MONGO_URI', 'mongodb://localhost:27017/testdb')

# Connect to the MongoDB server
client = MongoClient(mongo_uri)

# Access the database
db = client.get_default_database()


@app.route('/')
def index():
    # Example: Access a collection and retrieve a document
    collection = db['example_collection']
    document = collection.find_one()
    if document is None:
        return jsonify(message=f"Welcome to {env.capitalize()}")
    return jsonify(document)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
