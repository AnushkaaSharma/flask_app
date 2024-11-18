# tests/test_db_read.py
import pymongo
import pytest

def test_mongodb_ping():
    # Use your MongoDB URI from the .env file
    from os import getenv
    mongodb_uri = getenv("MONGODB_URI", "mongodb://localhost:27017/test")
    client = pymongo.MongoClient(mongodb_uri)
    try:
        client.admin.command('ping')  # Check MongoDB connection
        connected = True
    except Exception as e:
        connected = False
    assert connected, "MongoDB connection failed"
