#!/usr/bin/env python3
""" Script that provides some stats about Nginx logs stored in MongoDB """

from pymongo import MongoClient

if __name
client = MongoClient('mongodb://127.0.0.1:27017')
logs = client.logs.nginx
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

print('{} logs'.format(logs.estimated_document_count()))
print('Methods:')

for method in methods:
    print('\tmethod {}: {}'.format(
        method,
        logs.count_documents(filter={'method': method})))

print('{} status check'.format(logs.count_documents(filter={
    'method': 'GET',
    'path': '/status'})))
