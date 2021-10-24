import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

import pika
import json
from pika import connection
from pika import channel
from products.models import Product

params = pika.URLParameters('amqps://unylspen:zgATmXfU4d_Sq-Bc1AL_CISnqY_T7aQq@puffin.rmq2.cloudamqp.com/unylspen')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('Recieved in admin')
    id = json.loads(body)
    print(id)
    product = Product.objects.get(id=id)
    product.likes = product.likes + 1;
    product.save()
    print('Product likes increased')
     

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started consuming')

channel.start_consuming()
channel.close()