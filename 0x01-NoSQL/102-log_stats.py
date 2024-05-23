#!/usr/bin/env python3
""" Script that provides some stats about Nginx logs stored in MongoDB """

from pymongo import MongoClient
from itertools import islice

if __name__ == "__main__":
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

    print('IPs:')
    result = {}
    for log in logs.find():
        ip = log['ip']
        if ip in result:
            result[ip] += 1
        else:
            result[ip] = 1


    stats = sorted(result.items(), key=lambda x: x[1], reverse=True)
    top_ips = dict(islice(stats, 10))

    for key, value in top_ips.items():
        print('\t{}: {}'.format(key, value))
