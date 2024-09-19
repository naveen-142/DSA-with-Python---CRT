class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self):
        self.head=None
        self.next=None
    def addFirst(self,data):
        t=Node(data)
        if (self.head is None):
            self.head=t
            self.tail=t
        else:
            t.next=self.head
            self.head=t
    def display(self):
        currentNode=self.head
        while(currentNode is not None):
            print(currentNode.data,end="-->")
            currentNode=currentNode.next
sky=sll()
sky.addFirst(30)
sky.addFirst(20)
sky.addFirst(55)
sky.display()
