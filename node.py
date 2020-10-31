class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    def append(self, value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
        else:
            runner = self.head
            while runner.next != None:
                runner = runner.next
            runner.next = newNode
        return self

    def display(self):
        runner = self.head
        while runner != None:
            print(runner.value)
            runner = runner.next
        return self
    
    def removeFront(self):
        self.head = self.head.next
        return self

    def addFront(self, value):
        newNode=Node(value)
        newNode.next = self.head
        self.head = newNode
        return self

    def moveMin(self):
        if self.head == None:
            return self
        else:
            minval = self.head.value
            runner = self.head
            while runner.next != None:
                if runner.next.value < minval:
                    minval - runner.next.value
                    nodeBeforemin = runner
                    minNode = runner.next
                runner = runner.next
            nodeBeforemin.next = minNode.next
            minNode.next = self.head
            self.head = minNode
        return self

    def maxToBack(self):
        if self.head == None or self.head.next == None:
            return self
        elif self.head.next.next == None:
            rnr = self.head
            maxnode = self.head
            while rnr.next != None:
                rnr = rnr.next
            rnr.next = maxnode
            maxnode.next = None
            self.head = rnr
        else:
            maxval = self.head.value
            rnr = self.head
            while rnr.next != None:
                if rnr.next.value > maxval:
                    maxval = rnr.next.value
                    nodeBeforemax = rnr
                    maxNode = rnr.next
                rnr = rnr.next
            if self.head.value == maxval:
                rnr.next = self.head
                newhead = self.head.next
                self.head.next = None
                self.head = newhead
                return self
            nodeBeforemax.next = maxNode.next
            rnr.next = maxNode
            maxNode.next = None
        return self

newSll = SLL()
newSll.append(20).append(8).append(6).append(19).append(5).moveMin().moveMax().display()

# node1 = Node(5)
# node2 = Node(8)
# node1.next = node2
# node3 = Node(12)
# node2.next = node3

# print(node1.value)
# print(node1.next.value)
# print(node1.next.next.value)

# newSll.head = node1
# newSll.display()
# newSll.removeFront()
# print('removed the front')
# newSll.display()
