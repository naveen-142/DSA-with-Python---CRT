class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
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
            #self.head.prev=t              #  dll
            self.head=t
    def addlast(self,data):
        t=Node(data)
        if (self.tail is None):
            self.tail=t
            self.head=t
        else:
           # t.prev=self.tail            #dll
            self.tail.next=t
            self.tail=t
    def del_at_first(self,data):
        self.data=te
        te=self.head
        self.head=None

    def display(self):
        currentNode=self.head
        while(currentNode is not None):
            print(currentNode.data,end="-->")
            currentNode=currentNode.next
sky=sll()
sky.addFirst(30)
sky.addlast(40)
sky.addFirst(20)
sky.addlast(55)
sky.addFirst(69)
sky.addlast(10)
sky.addFirst(70)
sky.display()