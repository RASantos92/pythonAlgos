class Node:
	def __init__(self, value):
		self.value = value
		self.next = None


class Queue:
	def __init__(self):
		self.head = None
		self.tail = None

	def enqueue(self, value):
		#create new node
		newNode = Node(value)
		#check if queue is empty, if its empty-> set self.head and tail to point to it
		if self.head == None:
			self.head = newNode
			self.tail = newNode
		else:
			self.tail.next = newNode
			self.tail = self.tail.next
		return self

	def dequeue(self):
		if self.head == None:
			print("nothing to remove fam")
		else:
			valtoreturn = self.head.value
			self.head = self.head.next
			if self.head == None:
				self.tail = None
		return valtoreturn

	def size(self):
		runner = self.head
		count = 0
		while runner != None:
			count += 1
			runner = runner.next
		print(count)
		return count

	def display(self):
		runner = self.head
		# print(runner.next.next.next)
		while runner != None:
			print(runner.value)
			runner = runner.next
		print(runner)
		return self

	def isPalindrome(self):
		runner = self.head
		backward = []
		forward = []
		#creates array of queue elements going backwards
		while runner != None:
			backward.insert(0, runner.value)
			runner = runner.next
		#create array of queue elements going forward
		for i in range(len(backward)):
			forward.insert(0, backward[i])
		print(forward)
		print(backward)
		#checks if both arrays match each other
		if forward == backward:
			print(True)
			return True
		else:
			print(False)
			return False
		return self

	def contains(self, val):
		# if self.head == None:
		#     return False
		runner = self.head
		while runner != None:
			if runner.value == val:
				return True
			runner = runner.next
		return False
class Stack:
	def __init__(self):
		self.top = None

	def push(self, value):
		#create a new node
		newNode = Node(value)
		if self.top == None:
			self.top = newNode
		else:
			newNode.next = self.top
			self.top = newNode
		return self

	def pop(self):
		if self.top == None:
			print('nothing to pop doc')
			return self
		else:
			valToReturn = self.top.value
			self.top = self.top.next
		return valToReturn


	def size(self):
		runner = self.top
		count = 0
		while runner != None:
			count += 1
			runner = runner.next
		print(count)
		return count

	def display(self):
		runner = self.top
		# print(runner.next.next.next)
		while runner != None:
			print(runner.value)
			runner = runner.next
		print(runner)

# q1 = Queue()

# q1.enqueue(3).enqueue(84).enqueue(84).enqueue(3)
# q1.isPalindrome()

# q1 = Queue()

# q1.enqueue('h').enqueue('a').enqueue('n').enqueue('n').enqueue('a').enqueue('h')


def copyStack(stk):
	runner = stk.top
	temp=[]
	newStk = Stack()
	while runner != None:
		temp.append(runner.value)
		runner = runner.next
	print(len(temp))
	for i in range(len(temp)-1,-1,-1):
		newStk.push(temp[i])
	newStk.display()

stk = Stack()
stk.push(5).push(8).push(10).push(45).display()
copyStack(stk)
# outside of the calss function
# def palindrome(queueInput):
#     stk = Stack()
#     length = queueInput.size()
#     for i in range(length):
#         t = queueInput.dequeue()
#         queueInput.enqueue(t)
#         stk.push(t)
#     # print('-' * 40)
#     # stk.display()
#     # queueInput.display()
#     # print('-' * 40)
#     rnr = queueInput.head
#     rnr2 = stk.top
#     while rnr is not None:
#         if rnr.value is not rnr2.value:
#             print(False)
#             return False
#         rnr = rnr.next
#         rnr2 = rnr2.next
#     print(True)


# palindrome(q1)
