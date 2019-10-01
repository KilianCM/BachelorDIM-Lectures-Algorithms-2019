# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 08:31:57 2019

@author: chamiotk
"""

import os
import pika
import config
import getpass

def simple_queue_publish(concurrency = False, number = 1):
    ##
    #Function that send the username on the "presentation" queue using the url set in config.py 
    #Args:
    # @param concurrency 
    # @param number of message to send
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
    for i in range(number):
        channel.basic_publish(exchange='',
                              routing_key='presentation',
                              body=getpass.getuser(),
                              properties=properties)
        print(" [{i}] Sent '{username}'{persistent}".format(i=i+1, username=getpass.getuser(), persistent=str_persistent))
    connection.close()