# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 09:09:03 2019

@author: chamiotk
"""

import amqp_utils as amqp

def read_subscriber():
    connection = amqp.connection()
    channel = connection.channel()
    channel.exchange_declare(exchange='posts', exchange_type='fanout')
    result = channel.queue_declare(exclusive=True, queue="")
    queue_name = result.method.queue
        
    channel.queue_bind(exchange='posts', queue=queue_name)
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=False)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
    

def callback(ch, method, properties, body):
    print(" [x] %r" % body)


read_subscriber()