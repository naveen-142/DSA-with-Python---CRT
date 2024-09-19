class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
        self.tail=None
    '''def addfirst(self,data):
        t=Node(data)
        if (self.head is None):
            self.head=t
            self.tail=t
        else:
            t.next=self.head
            self.head=t'''
    def addlast(self,data):
        t=Node(data)
        if (self.tail is None):
            self.tail=t
            self.head=t
        else:
            self.tail.next=t
            self.tail=t
    def deletefirst(self):
        if(self.head is None):
            print("SLL is empty")
            return
        elif(self.head==self.tail):
            self.head=None
            self.tail=None
        else:
           self.head=self.head.next
    '''def deletelast(self):

        if (self.tail is None):
            print("SLL l is empty")
            return
        elif( self.tail==self.head):
            self.tail=None
            self.head=None
        else:
            temp=self.head
            while(temp.next is not None):
                prev=temp
                temp=temp.next
            prev.next=None
            self.tail=prev'''
    def peek(self):                    #peek operation prints the top element of stack
        print(self.tail.data)          #peek(): accessing the top element in the stack
    def display(self):
        temp=self.head
        while(temp is not None):
            print(temp.data,end="\t")
            temp=temp.next
b=SLL()
b.addlast(10)    #push(10)
b.addlast(20)    #push(20)
b.addlast(31)    #push(31)
b.addlast(40)    #push(40)
b.deletefirst()   #pop()
b.display()
print()
b.peek()

