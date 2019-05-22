import sys
# 数组的方法实现小顶堆
FRONT = 1
class MinHeap:
	def __init__(self, maxsize):
		self.maxsize = maxsize
		self.size = 0
		self.Heap = [None for i in range(maxsize+1)]
		# 小顶堆则插入-sys.maxsize，大顶堆则相反数
		self.Heap[0] = -sys.maxsize

	def _parent(self, pos):
		return pos//2

	def _leftChild(self, pos):
		return 2*pos

	def _rightChild(self, pos):
		return 2*pos+1

	def _isLeaf(self, pos):
		# return pos>=(self.size//2) and pos<=self.size
		if pos>=self.size//2 and pos<=self.size:
			return True
		return False

	def _swap(self, fpos, spos):
		self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

	# to heapify the node at pos
	def _minHeapify(self, pos):
		# if the node is non-leaf node and greater
		# than any of its child
		if not self._isLeaf(pos):
			if self.Heap[pos]>self.Heap[self._leftChild(pos)] \
				or self.Heap[pos]>self.Heap[self._rightChild(pos)]:
				# swap with the left child and heapify the left child
				if self.Heap[self._leftChild(pos)]<self.Heap[self._rightChild(pos)]:
					self._swap(pos, self._leftChild(pos))
					self._minHeapify(self._leftChild(pos))
				# swap with the right child and heapify the right child
				else:
					self._swap(pos, self._rightChild(pos))
					self._minHeapify(self._rightChild(pos))

	def insert(self, element):
		if self.size > self.maxsize:
			return False
		self.size += 1
		self.Heap[self.size] = element

		current = self.size
		while self.Heap[current] < self.Heap[self._parent(current)]:
			self._swap(current, self._parent(current))
			current = self._parent(current)

	def printHeap(self):
		for i in range(1, self.size//2+1):
			print("Parent:", self.Heap[i],
				"Left Child:", self.Heap[2*i],
				"Right Child:", self.Heap[2*i+1])

	def minHeap(self):
		for pos in range(self.size//2+1, 0, -1):
			self._minHeapify(pos)

	def remove(self):
		popped = self.Heap[FRONT]
		self.Heap[FRONT] = self.Heap[self.size-1]
		self.size -= 1
		self._minHeapify(FRONT)
		return popped

# driver code
if __name__ == '__main__':
	print('The Min Heap is:')
	minHeap = MinHeap(15)
	minHeap.insert(5)
	minHeap.insert(3)
	minHeap.insert(17)
	minHeap.insert(10)
	minHeap.insert(84)
	minHeap.insert(19)
	minHeap.insert(6)
	minHeap.insert(22)
	minHeap.insert(9)
	minHeap.minHeap()

	minHeap.printHeap()
	print('The Min value is:', minHeap.remove())