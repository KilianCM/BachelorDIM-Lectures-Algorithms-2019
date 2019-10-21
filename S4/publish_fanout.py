# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 08:46:41 2019

@author: chamiotk
"""

import amqp_utils as amqp

def publish_fanout():
    connection = amqp.connection()
    channel = connection.channel()
    channel.exchange_declare(exchange='posts', exchange_type='fanout')
    channel.basic_publish(exchange='posts', routing_key='key', body="This is a message")
    print("Sent message to posts exchange")

    
    
publish_fanout()