import pika
from pika import connection
from pika import channel
import json

params = pika.URLParameters('amqps://unylspen:zgATmXfU4d_Sq-Bc1AL_CISnqY_T7aQq@puffin.rmq2.cloudamqp.com/unylspen')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties) 