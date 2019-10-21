# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 08:31:57 2019

@author: chamiotk
"""

import pika
import getpass
import amqp_utils as amqp

def simple_queue_publish(concurrency = False, number = 1):
    ##
    #Function that send the username on the "presentation" queue using the url set in config.py 
    #Args:
    # @param concurrency 
    # @param number of message to send
    #Returns nothing
    connection = amqp.connection() 
    
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