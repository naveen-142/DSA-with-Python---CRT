class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
        self.tail=None
    def addfirst(self,data):
        t=Node(data)
        if (self.head is None):
            self.head=t
            self.tail=t
        else:
            t.next=self.head
            self.head=t
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
    def deletelast(self):
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
            self.tail=prev
    def display(self):
        temp=self.head
        while(temp is not None):
            print(temp.data,end="\t")
            temp=temp.next
b=SLL()
b.addlast(30)
b.addfirst(10)
b.addlast(11)
b.deletefirst()
b.deletelast()
b.addfirst(1)
b.display()

