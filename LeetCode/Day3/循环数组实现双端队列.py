class MyCircularDeque:

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.size = 0
        self.front = 0
        self.rear = k-1
        self.capacity = k
        self.Q = [None]*k

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            print('Full!')
            return False
        self.front = (self.front-1)%self.capacity
        self.Q[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            print('Full!')
            return False
        self.rear = (self.rear+1)%self.capacity
        self.Q[self.rear] = value
        self.size += 1
        return True

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            print('Empty!')
            return False
        self.Q[self.front] = None
        self.front = (self.front+1)%self.capacity
        self.size -= 1
        return True
        
    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            print('Empty!')
            return False
        self.Q[self.rear] = None
        self.rear = (self.rear-1)%self.capacity
        self.size -= 1
        return True
        
    def getFront(self):
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1
        value = self.Q[self.front]
        return value        

    def getRear(self):
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1
        value = self.Q[self.rear]
        return value        

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        """
        return self.size == 0
        
    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        """
        return self.size == self.capacity


# Your MyCircularDeque object will be instantiated and called as such:
k = 10
obj = MyCircularDeque(k)
param_1 = obj.insertFront(1)
param_2 = obj.insertLast(2)
param_3 = obj.deleteFront()
param_4 = obj.deleteLast()
param_5 = obj.getFront()
param_6 = obj.getRear()
param_7 = obj.isEmpty()
param_8 = obj.isFull()