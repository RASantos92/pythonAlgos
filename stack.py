class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, val):
        newNode = Node(val)
        if self.top == None:
            self.top = newNode
        else:
            temp = self.top 
            self.top = newNode
            newNode.next = temp
        return self
    
    def pop(self):
        if self.top == None:
            print("Nothing on top")
            return self
        else:
            returnVal = self.top.value
            self.top = self.top.next
        return self
    
    def size(self):
        runner = self.top
        count = 0
        while runner != None:
            count += 1
            runner = runner.next
        print("size", count)
        return count

    def display(self):
        runner = self.top
        while runner != None:
            print(runner.value)
            runner = runner.next
        return self

stk1 = Stack()
stk1.push(5).push(9).push(39).pop().display().size()