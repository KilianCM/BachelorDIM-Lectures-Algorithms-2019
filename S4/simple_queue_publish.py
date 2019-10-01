# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 08:31:57 2019

@author: chamiotk
"""

import os
import pika
import config
import getpass

def simple_queue_publish(concurrency):
    ##
    #Function that send the username on the "presentation" queue using the url set in config.py 
    #Returns nothing
    amqp_url=config.amqp_url
    
    url = os.environ.get('CLOUDAMQP_URL',amqp_url)
    params = pika.URLParameters(url)
    params.socket_timeout = 5
    
    connection = pika.BlockingConnection(params) # Connect to CloudAMQP
    
    properties = pika.BasicProperties()
    str_persistent = ""
    if concurrency:
        properties.delivery_mode = 2
        str_persistent = " with persistent mode"
    
    channel = connection.channel()
    channel.queue_declare(queue='presentation')
    channel.basic_publish(exchange='',
                          routing_key='presentation',
                          body=getpass.getuser(),
                          properties=properties)
    print(" [x] Sent '{username}'{persistent}".format(username=getpass.getuser(), persistent=str_persistent))
    connection.close()