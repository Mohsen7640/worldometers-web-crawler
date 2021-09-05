from mongo import MongoDatabase

from datetime import datetime


class MongoStorage:

    def __init__(self):
        self.mongo = MongoDatabase()

    def store(self, data, collection_name):
        collection = getattr(self.mongo.database, collection_name)
        if isinstance(data, list) and len(data) > 1:
            for record in data:
                collection.update_one(
                    filter={'country': record['country']},
                    update={'$set': {'date_updated': datetime.now()}},
                    upsert=True
                )
        else:
            collection.update_one(
                filter={'country': data['country']},
                update={'$set': {'date_updated': datetime.now()}},
                upsert=True
            )

    def load(self, filter_data, collection_name):
        collection = getattr(self.mongo.database, collection_name)
        if filter_data is None:
            return collection.find()
        return collection.find(filter_data)
