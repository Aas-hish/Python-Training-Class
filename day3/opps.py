class Student:
  
    def set_marks(self, marks):
        self.marks = marks

    def get_percentage(self):
        return self.marks/8
    

n= int(input("Enter the number of students: "))
marks = []
for i in range(n):
    s= Student()
    mark = int(input("Enter the marks of students: "))
    s.set_marks(mark)
    marks.append(s)
    
index=0
for i in marks:
    index += 1
    res = i.get_percentage()
    print("Percentage of student {} is: {}".format(index,res) )
    
  
    
    