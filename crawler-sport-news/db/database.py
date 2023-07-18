import os
from pymongo import MongoClient
from bson import ObjectId


class Database:

    def __init__(self):
        self.client = MongoClient(os.environ.get('STRING_CONNECTION_MONGO'))
        self.database_name = os.environ.get('DATABASE_NAME')

    def save_new_comment(self, _id, comment, status_game):
        try:
            collection_name = os.environ.get('COLLECTION_NAME')
            filter_value = {'_id': ObjectId(_id)}
            database = self.client[self.database_name]
            collection = database[collection_name]

            # data = collection.find_one(filter_value)
            # print("- ", data)
            timeline_push = {"$set": {"status": status_game}, "$push": {'timeline': comment}}
            print(timeline_push)

            collection.update_one(filter_value, timeline_push)

        except Exception as e:
            raise e

    def find_game_to_crawl(self, _id):
        try:
            collection_name = os.environ.get('COLLECTION_NAME')
            filter_value = {'_id': ObjectId(_id)}
            database = self.client[self.database_name]
            collection = database[collection_name]
            data_result = collection.find_one(filter=filter_value)
            return data_result

        except Exception as e:
            raise e

    def close_connection(self):
        self.client.close()
