# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 08:48:06 2019

@author: chamiotk
"""

import argparse
import simple_queue_publish as publish
import simple_queue_read as read


parser = argparse.ArgumentParser(description='Publish or read on presentation queue')
parser.add_argument('-r', '--read', action='store_true',
                    help='Read the presentation queue')
parser.add_argument('-p', '--publish', action='store_true',
                    help='Publish username on the presentation queue')
parser.add_argument('-c', '--concurrency', action='store_true',
                    help='Activate persitent messages')

args = parser.parse_args()

if(args.read):
    read.simple_queue_read()
elif(args.publish):
    publish.simple_queue_publish(args.concurrency)
else:
    print("Please specify -r to read or -p to publish")
