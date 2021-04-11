<<<<<<< HEAD
class Edge:   
    def __init__(self, ini,fim):
        self.ini = ini
        self.fim = fim
        self.processed = False
=======
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
>>>>>>> b9d086dcf13bab14be6122fbb6252a550b010552
        #print ("Objeto criado")
    
    def imprime(self):
        print("-------")
        self.ini.imprime()
        self.fim.imprime()
<<<<<<< HEAD
        print("--------")
    
=======
        print ("Fora" ,self.out)
        print("--------")
    
    def set(self, x, y, z):
        self.ini = x
        self.fim = y
        self.out = z

#P = Point()
#P.set(1,2)
#P.imprime()
#P.set(23,34,56)
#P.imprime()
>>>>>>> b9d086dcf13bab14be6122fbb6252a550b010552
