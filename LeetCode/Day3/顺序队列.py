# Python3 program for array implementation of queue 
class Queue: 
    def __init__(self, capacity): 
        self.front = self.size = 0
        self.rear = capacity -1
        self.Q = [None]*capacity 
        self.capacity = capacity 
    
    def is_full(self): 
        return self.size == self.capacity 
    
    # Queue is empty when size is 0 
    def is_empty(self): 
        return self.size == 0

    def enqueue(self, item): 
        if self.is_full(): 
            print("Full") 
            return
        self.rear = (self.rear + 1) % (self.capacity) 
        self.Q[self.rear] = item 
        self.size = self.size + 1
        print("%s enqueued to queue" %str(item)) 

    def dequeue(self): 
        if self.is_empty(): 
            print("Empty") 
            return
        
        print("%s dequeued from queue" %str(self.Q[self.front])) 
        self.front = (self.front + 1) % (self.capacity) 
        self.size = self.size -1
        
    # Function to get front of queue 
    def que_front(self): 
        if self.is_empty(): 
            print("Queue is empty") 

        print("Front item is", self.Q[self.front]) 
        
    # Function to get rear of queue 
    def que_rear(self): 
        if self.is_empty(): 
            print("Queue is empty") 
        print("Rear item is", self.Q[self.rear]) 


# Driver Code 
if __name__ == '__main__': 
    queue = Queue(30)
    
    queue.enqueue(10) 
    queue.enqueue(20) 
    queue.enqueue(30) 
    queue.enqueue(40) 
    queue.dequeue() 
    queue.que_front() 
    queue.que_rear() 
