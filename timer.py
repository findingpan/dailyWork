#!/usr/bin/python
import threading
import time

def func():
    print "this func will run 2 min."

while 1:
   	timer=threading.Timer(10, func)
   	timer.start()