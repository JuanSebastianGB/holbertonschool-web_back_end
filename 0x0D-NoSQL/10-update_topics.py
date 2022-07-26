#!/usr/bin/env python3

def update_topics(mongo_collection, name, topics):
    """ update_topics """
    mongo_collection.update_one(
        {'name': name},
        {'$set': {'topics': topics}})
