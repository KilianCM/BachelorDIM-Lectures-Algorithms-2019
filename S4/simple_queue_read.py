# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 08:37:24 2019

@author: chamiotk
"""

import os
import pika
import config
import time

def callback(ch, method, properties, body):
    ##
    #Function executed when a message enters in a queue and count the number of messages
    #Args:
    # @param ch
    # @param method
    # @param properties
    # @param body
    #Returns nothing
    print(" Message n{count} Received {body}".format(count=method.delivery_tag, body=body))
    ch.basic_ack(method.delivery_tag)

def slow_callback(ch, method, properties, body):
    ##
    #Function executed when a message enters in a queue and count the number of messages
    #Args:
    # @param ch
    # @param method
    # @param properties
    # @param body
    #Returns nothing
    print(" Message n{count} Received {body}".format(count=method.delivery_tag, body=body))
    ch.basic_ack(method.delivery_tag)
    time.sleep(1)

def simple_queue_read(concurrency, slow = False):
    ##
    #Function that listens the "presentation" queue using the url set in config.py and print each message 
    #Args:
    #   @param concurrency
    #Returns nothing
    amqp_url=config.amqp_url
    
    url = os.environ.get('CLOUDAMQP_URL',amqp_url)
    params = pika.URLParameters(url)
    params.socket_timeout = 5
    
    connection = pika.BlockingConnection(params) # Connect to CloudAMQP
        
    channel = connection.channel()
    channel.queue_declare(queue='presentation')
    
    if slow:
        channel.basic_consume(queue='presentation',
                              on_message_callback=slow_callback,                 
                              auto_ack=False)
    else:
        channel.basic_consume(queue='presentation',
                              on_message_callback=callback,                 
                              auto_ack=False)
        
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

