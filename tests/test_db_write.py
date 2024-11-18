# tests/test_db_write.py
import pymongo
import pytest

def test_mongodb_write():
    # Use your MongoDB URI from the .env file
    from os import getenv
    mongodb_uri = getenv("MONGODB_URI", "mongodb://localhost:27017/test")
    client = pymongo.MongoClient(mongodb_uri)
    db = client.test_db  # Replace with your database name
    collection = db.test_collection  # Replace with your collection name

    # Insert a test document
    test_document = {"name": "Test", "value": 42}
    insert_result = collection.insert_one(test_document)

    # Query the database to confirm insertion
    retrieved_doc = collection.find_one({"_id": insert_result.inserted_id})
    assert retrieved_doc is not None, "Document not found in the database"
    assert retrieved_doc["name"] == "Test", "Document name mismatch"
    assert retrieved_doc["value"] == 42, "Document value mismatch"

    # Cleanup: Remove the test document
    collection.delete_one({"_id": insert_result.inserted_id})