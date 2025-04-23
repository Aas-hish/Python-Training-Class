
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Linkedlist:
    def __init__(self):
        self.head = None
        
    def insert(self, data):
        if(not self.head):
            new_node = Node(data)
            self.head=new_node
        else:
            temp = self.head
            while(temp.next):
                temp=temp.next
            new_node = Node(data)
            temp.next = new_node
        print("{} is inserted".format(data))
    
    def display(self):
        res=[]
        temp= self.head
        
        while(temp):
            res.append(temp.data)
            temp=temp.next
        print(" ---> ".join(map(str,res)))
            

l= Linkedlist()
l.insert(100)
l.insert(300)
l.insert(900)
l.display()