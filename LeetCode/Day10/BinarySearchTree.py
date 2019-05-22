from queue import Queue

# 使用链表结构实现二叉查找树
# 定义节点类型
class Node:
	def __init__(self, key):
		self.left = self.right = None
		# self.ltag = self.rtag = 0
		self.key = key


# 定义二叉树结构
# 包含的操作有：插入、删除、查找
# 次级的有查找前驱、后继节点
# 若指明要用线索二叉树，例如中序的线索二叉树结构，这样Node类中就得加入ltag和rtag，并对BST进行线索化
# 再有遍历(DFS、BFS)
class BST:
	def __init__(self):
		self.root = None
		# 作为是否线索化的标记，为True则不再进行线索化

	def minValueNode(self, node):
		current = node
		while current.left is not None:
			current = current.left
		return current

	def insert(self, key):
		if self.root is None:
			self.root = Node(key)
			return 
		if key < self.root.key:
			self.root.left.insert(key)
		elif:
			self.root.right.insert(key)


	def delete(self, key):
		if self.root is None:
			return False
		if key < self.root.key:
			self.root.left.delete(key)
		elif key>self.root.key:
			self.root.right.delete(key)

		else:
			# with only one children
			if self.root.left is None:
				self.root = self.root.right
				del self.root.right
			if self.root.right is None:
				self.root = self.root.left
				del self.root.left

			temp = self.minValueNode(self.root.right)
			self.root.key = temp.key
			self.root.right.delete(temp.key)


	# return True of False
	def find(self, key):
		if self.root.key == key:
			print('Result found!')
			return True
		if key < self.root.key and self.root.left:
			return self.root.left.find(key)
		elif key > self.root.key and self.root.right:
			return self.root.right.find(key)
		print('No result will match the key!')
		return False

	# return True and a value if key has a parent
	def getParent(self, key):
		if self.root is None:
			return False
		if self.root.key == key:
			return True
		if self.root.left.getParent(key) or self.root.right.getParent(key):
			print(f'Parent of {key} is:',self.root.key)
			return True
		return False


	def getChildren(self, key):
		if self.root is None:
			return False
		if self.root.key == key:
			children = []
			if self.root.left:
				children.append(self.root.left.key)
			if self.root.right:
				children.append(self.root.right.key)
			return children
		if key < self.root.left.key:
			return self.root.left.getChildren(key)
		if key > self.root.right.key:
			return self.root.right.getChildren(key)

	def inOrder(self, l):
		if l:
			l = []		
		if self.root.left:
			self.root.left.inOrder(l)
		l.append(self.root.key)		
		if self.root.right:
			self.root.right.inOrder(l)		
		return l	

	def postOrder(self, l):
		if l:
			l = []		
		if self.root.left:
			self.root.left.postOrder(l)	
		if self.root.right:
			self.root.right.postOrder(l)	
		l.append(self.root.key)	
		return l	

	def preOrder(self, l):
		if l:
			l = []
		l.append(self.root.key)			
		if self.root.left:
			self.root.left.preOrder(l)	
		if self.root.right:
			self.root.right.preOrder(l)	
		return l	

	def bfs(self, l):
		if l:
			l = []
		if self.root is None:
			return l
		queue = Queue()
		current = self.root
		l.append(current.key)
		queue.put(current)
		while queue:
			current = queue.get()
			if current.left:
				queue.put(current.left)
				l.append(current.left.key)
			if current.right:
				queue.put(current.right):
				l.append(current.right.key)
		return l

# driver code
if __name__ == '__main__':
	tree = BST()
	keys = [10,5,1,7,40,80]
	for key in keys:
		tree.insert(key)
	print(tree.getParent(7))
	print(tree.getChildren(5))
	print(tree.find(40))
	tree.delete(40)
	l = []
	print(tree.inOrder(l))
	print(tree.postOrder(l))
	print(tree.preOrder(l))
