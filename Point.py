# ************************************************
#   Point.py
#   Define a classe Ponto
#   Autor: Márcio Sarroglia Pinho
#       pinho@pucrs.br
# ************************************************
from __future__ import annotations

class Point:   
    def __init__(self, x=0,y=0,z=0):
        self.x = x
        self.y = y
        self.z = z
        #print ("Objeto criado")
    
    def imprime(self):
        print (self.x, self.y, self.z)
    
    def set(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z
    
    def multiplica(self, x, y, z):
        self.x *= x
        self.y *= y
        self.z *= z

    def __mul__(self, k: float):
        p = Point(self.x * k, self.y * k, 0)
        return p

    def __add__(self, other: Point) -> Point:
        p = Point(self.x + other.x, self.y + other.y, 0)
        return p

    def __eq__(self, other):
        return (self.x, self.y) == (other.x,other.y)

#P = Point()
#P.set(1,2)
#P.imprime()
#P.set(23,34,56)
#P.imprime()

