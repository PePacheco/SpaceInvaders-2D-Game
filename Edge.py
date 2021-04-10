class Edge:   
    def __init__(self, ini,fim):
        self.ini = ini
        self.fim = fim
        self.processed = False
        #print ("Objeto criado")
    
    def imprime(self):
        print("-------")
        self.ini.imprime()
        self.fim.imprime()
        print("--------")
    