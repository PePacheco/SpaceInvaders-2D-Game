# ************************************************
#   Poligonos.py
#   Define a classe Polygon
#   Autor: Márcio Sarroglia Pinho
#       pinho@pucrs.br
# ************************************************
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from Point import *
import copy

def loadEnemies():
    enemy1 = Polygon()
    enemy1.insereVertice(0, 0, 0)
    enemy1.insereVertice(0, 8, 0)
    enemy1.insereVertice(8, 8, 0)
    enemy1.insereVertice(8, 0, 0)
    enemy2 = Polygon()
    enemy2.insereVertice(0, 0, 0)
    enemy2.insereVertice(0, 6, 0)
    enemy2.insereVertice(7, 6, 0)
    enemy2.insereVertice(7, 0, 0)
    enemy3 = Polygon()
    enemy3.insereVertice(0, 0, 0)
    enemy3.insereVertice(0, 6, 0)
    enemy3.insereVertice(7, 6, 0)
    enemy3.insereVertice(7, 0, 0)
    enemy4 = Polygon()
    enemy4.insereVertice(0, 0, 0)
    enemy4.insereVertice(0, 8, 0)
    enemy4.insereVertice(8, 8, 0)
    enemy4.insereVertice(8, 0, 0)
    enemy5 = Polygon()
    enemy5.insereVertice(0, 0, 0)
    enemy5.insereVertice(0, 6, 0)
    enemy5.insereVertice(7, 6, 0)
    enemy5.insereVertice(7, 0, 0)
    enemy6 = Polygon()
    enemy6.insereVertice(0, 0, 0)
    enemy6.insereVertice(0, 6, 0)
    enemy6.insereVertice(7, 6, 0)
    enemy6.insereVertice(7, 0, 0)
    enemy7 = Polygon()
    enemy7.insereVertice(0, 0, 0)
    enemy7.insereVertice(0, 8, 0)
    enemy7.insereVertice(8, 8, 0)
    enemy7.insereVertice(8, 0, 0)
    enemy8 = Polygon()
    enemy8.insereVertice(0, 0, 0)
    enemy8.insereVertice(0, 6, 0)
    enemy8.insereVertice(6, 6, 0)
    enemy8.insereVertice(6, 0, 0)
    enemy9 = Polygon()
    enemy9.insereVertice(0, 0, 0)
    enemy9.insereVertice(0, 6, 0)
    enemy9.insereVertice(7, 6, 0)
    enemy9.insereVertice(7, 0, 0)
    enemy10 = Polygon()
    enemy10.insereVertice(0, 0, 0)
    enemy10.insereVertice(0, 6, 0)
    enemy10.insereVertice(7, 6, 0)
    enemy10.insereVertice(7, 0, 0)

    return [enemy1, enemy2, enemy3, enemy4, enemy5, enemy6, enemy7, enemy8, enemy9, enemy10]

def loadBuildings():
    building1 = Polygon()
    building1.insereVertice(30, 0, 0)
    building1.insereVertice(30, 27, 0)
    building1.insereVertice(33, 27, 0)
    building1.insereVertice(33, 0, 0)
    building2 = Polygon()
    building2.insereVertice(40, 0, 0)
    building2.insereVertice(40, 16, 0)
    building2.insereVertice(51, 16, 0)
    building2.insereVertice(51, 0, 0)
    building3 = Polygon()
    building3.insereVertice(55, 0, 0)
    building3.insereVertice(55, 27, 0)
    building3.insereVertice(58, 27, 0)
    building3.insereVertice(58, 0, 0)
    building4 = Polygon()
    building4.insereVertice(65, 0, 0)
    building4.insereVertice(65, 16, 0)
    building4.insereVertice(76, 16, 0)
    building4.insereVertice(76, 0, 0)
    building5 = Polygon()
    building5.insereVertice(80, 0, 0)
    building5.insereVertice(80, 27, 0)
    building5.insereVertice(83, 27, 0)
    building5.insereVertice(83, 0, 0)
    building6 = Polygon()
    building6.insereVertice(87, 0, 0)
    building6.insereVertice(87, 16, 0)
    building6.insereVertice(98, 16, 0)
    building6.insereVertice(98, 0, 0)

    return [building1, building2, building3, building4, building5, building6]

class Polygon:

    def __init__(self, center: Point = Point()):
        self.vertices = []
        self.edges = []
        self.center = center
        self.translate = Point()

    def setCenter(self, center: Point):
        self.center = center

    def setTranslate(self, translate: Point):
        self.translate = translate

    def getNVertices(self):
        return len(self.Vertices)

    def insereVertice(self, x, y, z):
        self.vertices += [Point(x,y,z)]

    def insereVerticePosition(self, x,y,z,position):
        if  position < 0 or position > len(self.Vertices):
            print('Posicao Invalida. Vertice nao inserido.')
            return
        self.vertices.insert(position,Point(x,y,z))

    def desenhaPoligono(self):
        #print ("Desenha Poligono - Tamanho:", len(self.Vertices))
        glBegin(GL_LINE_LOOP)
        for V in self.vertices:
            glVertex3f(V.x,V.y,V.z)
        glEnd()

    def desenhaVertices(self):
        glBegin(GL_POINTS);
        for V in self.vertices:
            glVertex3f(V.x,V.y,V.z);
        glEnd()

    def imprimeVertices(self):
        for y in self.vertices:
            y.imprime()

    def getLimits(self):
        Min = copy.deepcopy(self.vertices[0])
        Max = copy.deepcopy(self.vertices[0])
        for V in self.vertices:
            if V.x > Max.x:
                Max.x = V.x
            if V.y > Max.y:
                Max.y = V.y
            if V.z > Max.z:
                Max.z = V.z
            if V.x < Min.x:
                Min.x = V.x
            if V.y < Min.y:
                Min.y = V.y
            if V.z < Min.z:
                Min.z = V.z
        # print(Min)
        # Min.imprime()
        # Max.imprime()
        return Min, Max
