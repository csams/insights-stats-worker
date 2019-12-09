#!/usr/bin/env python
import pika
import os
import yaml

Loader = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

params = pika.ConnectionParameters(host='localhost', port=5672)
connection = pika.BlockingConnection(params)

channel = connection.channel()
channel.queue_declare(queue='test_job')

root = "/home/csams/Downloads/archives/insights/"
archives = []

for archive in archives:
    path = os.path.join(root, archive)
    msg = {"url": path}
    body = yaml.dump(msg)
    channel.basic_publish(exchange='', routing_key="test_job", body=body)
connection.close()
