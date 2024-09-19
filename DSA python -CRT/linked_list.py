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
    def diff(self):
        t=self.head
        se=0
        so=0
        while(t!=None):
            if (t.data%2==0):
                se=se+t.data
            else:
                so=so+t.da


l=sll()
n=int(input())

for i in range(5):
    print(l.add_back())

