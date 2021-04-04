# ************************************************
#   Edge.py
#   Define a classe Ponto
#   Autor: Márcio Sarroglia Pinho
#       pinho@pucrs.br
# ************************************************


class Edge:   
    def __init__(self, ini,fim,out):
        self.ini = ini
        self.fim = fim
        self.out = out
        #print ("Objeto criado")
    
    def imprime(self):
        self.ini.imprime()
        self.fim.imprime()
        print (self.out)
    
    def set(self, x, y, z):
        self.ini = x
        self.fim = y
        self.out = z

#P = Point()
#P.set(1,2)
#P.imprime()
#P.set(23,34,56)
#P.imprime()