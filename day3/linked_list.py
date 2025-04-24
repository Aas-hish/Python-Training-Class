
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
    
    def insertAtpos(self, data, pos):
        if(not self.head):
            print("List is empty")
            return
        if(pos==1):
            new_node = Node(data)
            new_node.next= self.head
            self.head = new_node
            return
        
        temp = self.head
        for i in range(1,pos-1):
            if not temp:
                print("Position out of range")
                return
            temp = temp.next

        if not temp:
            print("Position out of range")
            return
        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node
        

l= Linkedlist()
l.insert(100)
l.insert(300)
l.insert(900)
l.insertAtpos(500,4)
l.display()