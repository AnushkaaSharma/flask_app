import os
import unittest
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

"""
Unit tests for MongoDB write operations.
- Tests document insertion into a test database and verifies its correctness.
- Ensures that the inserted document can be retrieved and matches the original data.
- Uses a dedicated test database to avoid affecting production data.
- Cleans up the test database after the test completes.
"""

class TestMongoDBWriteOperation(unittest.TestCase):
    def setUp(self):
        """
        Set up the MongoDB connection and create a test database and collection.
        """
        self.connection_string = f"mongodb+srv://{os.getenv('MONGODB_USERNAME')}:{os.getenv('MONGODB_PASSWORD')}@cluster0.oglqn.mongodb.net"
        self.client = MongoClient(self.connection_string)
        self.db = self.client["test_db"]  # Create a test database
        self.collection = self.db["test_product"]  # Create a test collection

    def test_insert_and_retrieve_document(self):
        """
        Test the insertion of a sample document into MongoDB.
        Verify that the inserted document can be queried and matches the original data.
        """
        # Sample test document
        test_product = {
            "name": "Key Halter Mini Dress",
            "image_path": "../static/images/product1.png",
            "price": 29.99,
        }

        # Insert the document into the collection
        insert_response = self.collection.insert_one(test_product)

        # Verify that the insertion was successful by checking the returned ID
        self.assertIsNotNone(insert_response.inserted_id, "Document insertion failed.")

        # Query the inserted document by its ID
        query_response = self.collection.find_one({"_id": insert_response.inserted_id})

        # Assert that the retrieved document matches the original
        self.assertEqual(query_response["name"], test_product["name"])
        self.assertEqual(query_response["image_path"], test_product["image_path"])
        self.assertEqual(query_response["price"], test_product["price"])

    def tearDown(self):
        """
        Clean up after the test:
        - Drop the test collection.
        - Close the MongoDB connection.
        """
        self.collection.drop()
        self.client.close()

if __name__ == "__main__":
    unittest.main()