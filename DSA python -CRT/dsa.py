class new_node:
    def __init__(self,x):
        self.data=x
        self.nxt=None
class sll:
    def __init__(self):
        self.head=None
    def add_back(self,x):
        if self.head==None:
            self.head=new_node(x)
        else:
            temp=self.head
            while(temp.nxt!=None):
                temp=temp.nxt
            temp.nxt=new_node(x)
    def add_front(self,x):
        temp=new_node(x)
        temp.nxt=self.head
        self.head=temp
    def display(self):
        temp=self.head
        while(temp!=None):
            print(temp.data)
            temp=temp.nxt
l=sll()
l.add_back(10)
l.add_back(20)
l.add_front(50)
l.add_back(30)
l.display()
