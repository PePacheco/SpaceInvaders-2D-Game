from Point import *

class AABB:   
    def __init__(self, center: Point = Point(0,0,0), halfWidth: Point = Point(0,0,0)):
        self.center = center
        self.halfWidth = halfWidth
    
    def set(self, center: Point, halfWidth: Point):
        self.center = center
        self.halfWidth = halfWidth

    def imprime(self):
        self.center.imprime()
        self.halfWidth.imprime()

    def __eq__(self, other):
        return (self.center, self.halfWidth) == (other.center,other.halfWidth)