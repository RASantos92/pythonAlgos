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
            self.head = self.head.next
            if self.head == None:
                self.tail = None
        return self

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

    def contains(self, val):
        runner = self.head
        while runner != None:
            if val == runner.value:
                print("Its in here")
                break
            else:
                print("Its not in here")
                break
        return self







q1 = Queue()
q2 = Queue()
q2.enqueue(8)
q2.dequeue()


q1.enqueue(5).enqueue(15).enqueue(25).display()
print("*******")
q1.size()
q1.contains(5)