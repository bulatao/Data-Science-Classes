import copy

class Point():
    '''Represeting a 2D point with an x and y coordinate'''

def print_point(p):
    print("(%.1f, %.1f)" %(p.x, p.y))

class Rectangle():
    '''Representing a rectangle with width and height'''

    def __init__(self, width, height):
        self.width = width
        self.height = height
        

    def print_rectangle(self):
        print("width = %.1f hieght = %.1f" % (self.width, self.height))

    def total_area(self, other):
        area1 = self.width * self.height
        area2 = other.width * other.height
        return area1 + area2

def tester():
    
    rect1 = Rectangle()
    rect1.width = 5
    rect1.height = 8
    rect2 = Rectangle()
    rect2.width = 12
    rect2.height = 11
    rect1.print_rectangle()
    rect2.print_rectangle()
    area = Rectangle.total_area(rect1,rect2)
    print("area=", area)


def print_rectangle(rect):
    print("width = %.1f height = %.1f corner = (%.1f,%1.f)" % (rect.width, rect.height, rect.corner.x, rect.corner.y))

def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.height/2
    return copy.copy(p)

class Car:
    '''Represents a new type Car'''

def print_car(c):
    print("maker is %s, with a fuel capacity of %i and %i number of doors" % (c.maker, c.fuelcapacity, c.no_of_doors))
    
def which_is_bigger(rect, rect2):
    area1 = rect1.width * rect1.height
    area2 = rect2.width * rect2.height
    if area1 > area2:
        return copy.deepcopy(rect1)
    else:
        return copy.deepcopy(rect2)
