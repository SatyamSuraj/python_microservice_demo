import pika
from pika import connection
from pika import channel

params = pika.URLParameters('amqps://unylspen:zgATmXfU4d_Sq-Bc1AL_CISnqY_T7aQq@puffin.rmq2.cloudamqp.com/unylspen')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('Recieved in admin')
    print(body) 

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started consuming')

channel.start_consuming()
channel.close()