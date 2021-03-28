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


class Polygon:

    def __init__(self):
        self.Vertices = []
        self.Arestas = { 'out': [], 'in': [] }

    def getNVertices(self):
        return len(self.Vertices)
    
    #def insereVertice(self, P):
    #    temp = copy.deepcopy(P)
    #    self.Vertices += [temp]

    def insereVertice(self, x, y, z):
        self.Vertices += [Point(x,y,z)]

    def insereVerticePosition(self, x,y,z,position):
        if  position < 0 or position > len(self.Vertices):
            print('Posicao Invalida. Vertice nao inserido.')
            return
        self.Vertices.insert(position,Point(x,y,z))

    def desenhaPoligono(self):
        #print ("Desenha Poligono - Tamanho:", len(self.Vertices))
        glBegin(GL_LINE_LOOP);
        for V in self.Vertices:
            glVertex3f(V.x,V.y,V.z);
        glEnd();

    def desenhaVertices(self):
        glBegin(GL_POINTS);
        for V in self.Vertices:
            glVertex3f(V.x,V.y,V.z);
        glEnd();

    def imprimeVertices(self):
        for y in self.Vertices:
            y.imprime()

    def getLimits(self):
        Min = copy.deepcopy(self.Vertices[0])
        Max = copy.deepcopy(self.Vertices[0])
        for V in self.Vertices:
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
        print("getLimits")
        #Min.imprime()
        #Max.imprime()
        return Min, Max
