# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 09:15:13 2019

@author: chamiotk
"""
import os
import pika
import config

def connection():
    amqp_url=config.amqp_url
    url = os.environ.get('CLOUDAMQP_URL',amqp_url)
    params = pika.URLParameters(url)
    params.socket_timeout = 5
    
    connection = pika.BlockingConnection(params) # Connect to CloudAMQP
    return connection
    