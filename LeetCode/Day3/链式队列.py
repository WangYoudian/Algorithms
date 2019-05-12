# Python3 program to demonstrate linked list 

# A linked list (LL) node 
# to store a queue entry 
class Node: 
	def __init__(self, data): 
		self.data = data 
		self.next = None

# The queue, front stores the front node 
# of LL and rear stores ths last node of LL 
class Queue: 
	
	def __init__(self): 
		self.front = self.rear = None

	def is_empty(self): 
		return self.front == None
	
	# Method to add an item to the queue 
	def enqueue(self, item): 
		temp = Node(item) 
		if self.rear == None: 
			self.front = self.rear = temp 
			return
		self.rear.next = temp 
		self.rear = temp 

	# Method to remove an item from queue 
	def dequeue(self): 
		if self.is_empty(): 
			return
		temp = self.front 
		self.front = temp.next

		# After dequeue, the queue is empty now
		if self.front == None: 
			self.rear = None
		return str(temp.data) 

# Driver Code 
if __name__== '__main__': 
	q = Queue() 

	q.enqueue(10) 
	q.enqueue(20) 
	q.dequeue() 
	q.dequeue() 
	q.enqueue(30) 
	q.enqueue(40) 
	q.enqueue(50) 
	
	print("dequeued item is " + q.dequeue()) 
	
