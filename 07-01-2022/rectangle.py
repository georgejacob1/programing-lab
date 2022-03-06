class rectangle:
    def __init__(self,l1,b1):
        self.length=l1
        self.breadth=b1
    def area(self):
        return(self.length*self.breadth)
    def perimeter(self):
        print("Perimeter=", 2*(self.length+self.breadth))
    def compare(self,obj):
        if(self.area()>obj.area()):
            print("Rectangle1 is large!!")
        else:
            print("Rectangle2 is large!!")
R1=rectangle(2,5)
R1.area()
R1.perimeter()
R2=rectangle(4,8)
R2.area()
R2.perimeter()
R1.compare(R2)