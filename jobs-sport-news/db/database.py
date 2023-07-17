import os
from pymongo import MongoClient
from datetime import datetime


class Database:

    def __init__(self):
        self.client = MongoClient(os.environ.get('STRING_CONNECTION_MONGO'))
        self.database_name = os.environ.get('DATABASE_NAME')

    def find_all_games_to_start(self):
        try:
            collection_name = os.environ.get('COLLECTION_NAME')
            filter_value = {'status': 'TO_START', "date": {"$lt": datetime.now()}}
            database = self.client[self.database_name]
            collection = database[collection_name]
            data_result = list(collection.find(filter=filter_value))
            return data_result

        except Exception as e:
            raise e

    def close_connection(self):
        self.client.close()
