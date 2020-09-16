#last in first out##


from collections import deque

class Queue:
    def __init__(self):
        self.buffer=deque()

    def enqueue(self , value):
        self.buffer.appendleft(value)

    def dequeue(self):
        print(self.buffer.pop())

    def is_empty(self):
        print(len(self.buffer)==0)
    
    def length(self):
        print(len(self.buffer))


pq=Queue()
pq.enqueue({
    'company': 'wall mart',
    'timestamp': '1:23:4',
    'price': 786
})    

pq.enqueue({
    'company': 'nifty',
    'timestamp': '9:3:20',
    'price': 67864
})    

pq.enqueue({
    'company': 'India Mart',
    'timestamp': '8:14:5',
    'price': 674
})    

pq.buffer
pq.dequeue()
pq.length()