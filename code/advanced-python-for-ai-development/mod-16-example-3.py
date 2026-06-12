from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['ml_database']
collection = db['predictions']

# Insert
doc = {
    'model_id': 'v1',
    'timestamp': datetime.now(),
    'prediction': 0.95
}
collection.insert_one(doc)

# Query
results = list(collection.find({'model_id': 'v1'}))