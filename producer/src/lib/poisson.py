import math
import random
import time
import random
from multiprocessing import Queue
from threading import Thread


queue = Queue(100)

# Borrowed from https://www.agiliq.com/blog/2013/10/producer-consumer-problem-in-python/?utm_source=agiliq&utm_medium=twitter

def next_arrival_time(rateParameter=40):
    return -math.log(1.0 - random.random()) / rateParameter

# code to test unit test
#class ProducerThread(Thread):
#    def run(self):
#        global queue
#        next_time = poisson()
#        arrival_interval = 0
#        for num in range(0,13):
#            arrival_interval = arrival_interval + poisson()
#            time.sleep(arrival_interval)
#            queue.put(num)
#            print("Job ID: workload-%s produced at %s seconds" %(num,
#                  int(arrival_interval)))
#
#
#ProducerThread().start()
