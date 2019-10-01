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
parser.add_argument('-n', type=int, default=1, action='store',
                    help='Number of messages to send (default 1)')
args = parser.parse_args()

if(args.read):
    read.simple_queue_read(args.concurrency)
elif(args.publish):
    publish.simple_queue_publish(args.concurrency, args.n)
else:
    print("Please specify -r to read or -p to publish")
