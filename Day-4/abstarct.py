class shape:
    def area(self):
        pass
class rectangele(shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        print("area",self.l*self.b)
class circle(shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        print("area",3.14*self.r*self.r)
rect = rectangele(10, 5)
circle = circle(7)
rect.area()
circle.area()