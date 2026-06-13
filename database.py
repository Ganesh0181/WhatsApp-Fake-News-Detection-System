from pymongo import MongoClient
from datetime import datetime

client = MongoClient(
    "mongodb://localhost:27017/"
)

db = client["fake_news_db"]

collection = db["predictions"]

def save_result(
    phone,
    text,
    prediction,
    confidence
):

    data = {
        "phone": phone,
        "text": text,
        "prediction": prediction,
        "confidence": confidence,
        "time": datetime.now()
    }

    collection.insert_one(data)