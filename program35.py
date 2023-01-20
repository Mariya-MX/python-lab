class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)

l=int(input("Enter the length : "))
b=int(input("Enter the breadth : "))
r=rectangle(l,b)
y=r.area()
x=r.perimeter()
print("Area is ",y)
print("Perimeter is ",x)

l1=int(input("Enter the length : "))
b1=int(input("Enter the breadth : "))
r1=rectangle(l,b)
y1=r1.area()
x1=r1.perimeter()
print("Area is ",y1)
print("Perimeter is ",x1)

if y>y1:
    print("First Rectangle is greater")
else:
    print("Second Rectangle is greater")


