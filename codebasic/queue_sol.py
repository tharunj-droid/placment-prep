'''Design a food ordering system where your python program will run two threads,

Place Order: This thread will be placing an order and inserting that into a queue. This thread places new order every 0.5 second. (hint: use time.sleep(0.5) function)
Serve Order: This thread will server the order. All you need to do is pop the order out of the queue and print it. This thread serves an order every 2 seconds. Also start this thread 1 second after place order thread is started.
Use this video to get yourself familiar with multithreading in python

Pass following list as an argument to place order thread,

orders = ['pizza','samosa','pasta','biryani','burger']'''
import time
from collections import deque


class Food_order:
    def __init__(self, food_item):
        self.buffer = deque()
        self.food_item = food_item
        

    def place_order(self, food_item):
        self.buffer.appendleft(food_item)

    def delivery(self):
        if len(self.buffer)==0:
            print("buffer is empty")
            quit()


        return self.buffer.pop()
    
    def size(self):
        return len(self.buffer)


order = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']
queue = Food_order(order)

for x in order:
    queue.place_order(x)
    time.sleep(0.5)

while True:
    time.sleep(2)
    print(queue.delivery())