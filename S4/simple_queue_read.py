# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 08:37:24 2019

@author: chamiotk
"""

import os
import pika
import config


count=0

def callback(ch, method, properties, body):
    ##
    #Function executed when a message enters in a queue and count the number of messages
    #Args:
    # @param ch
    # @param method
    # @param properties
    # @param body
    #Returns nothing
    global count
    count += 1
    print(" Message n{count} Received {body}".format(count=count, body=body))


def simple_queue_read():
    ##
    #Function that listens the "presentation" queue using the url set in config.py and print each message 
    #Returns nothing
    amqp_url=config.amqp_url
    
    url = os.environ.get('CLOUDAMQP_URL',amqp_url)
    params = pika.URLParameters(url)
    params.socket_timeout = 5
    
    connection = pika.BlockingConnection(params) # Connect to CloudAMQP
    
    channel = connection.channel()
    channel.queue_declare(queue='presentation')
    channel.basic_consume(queue='presentation',
                          on_message_callback=callback,                          
                          auto_ack=True)
        
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

