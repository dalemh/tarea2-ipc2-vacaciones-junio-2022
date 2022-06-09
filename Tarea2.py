
class Node:
    def __init__(self, x):
        self.objeto = x
        self.sigueinte = None
        self.anterior = None
 

class listadoble:
    def __init__(self):
        self.nodoinicial = None

    def ingresovacio(self, x):
        if self.nodoinicial is None:
            nuevonodo = Node(x)
            self.nodoinicial = nuevonodo
        else:
            print("Lista vacía")


    def ingreso_al_final(self, x):

        if self.nodoinicial is None:
            nuevonodo = Node(x)
            self.nodoinicial = nuevonodo
            return
        n = self.nodoinicial

        while n.sigueinte is not None:
            n = n.sigueinte
        nuevonodo = Node(x)
        n.sigueinte = nuevonodo
        nuevonodo.anterior = n
   
 
    def imprimir(self):
        if self.nodoinicial is None:
            print("El nodo esta vacío")
            return
        else:
            n = self.nodoinicial
            while n is not None:
                print( n.objeto)
                n = n.sigueinte
        print("\n")
    
    def imprimirejercicio(self,x):
        if self.nodoinicial is None:
            print("Lista Vacía")
            return
        else:
            n = self.nodoinicial
            while n is not None :
                
                if n.objeto == x :
                    n= n.anterior
                    print(n.objeto)
                    n= n.sigueinte
                    print(n.objeto)
                    n= n.sigueinte
                    print(n.objeto)
                    
                n = n.sigueinte
                
        print("\n")



nuevalistadoble = listadoble()
nuevalistadoble.ingreso_al_final(int(2))
nuevalistadoble.ingreso_al_final(int(7))
nuevalistadoble.ingreso_al_final(int(5))
nuevalistadoble.ingreso_al_final(int(11))
nuevalistadoble.ingreso_al_final(int(4))
nuevalistadoble.imprimir()
posicion = int(input('ingrese número: '))
nuevalistadoble.imprimirejercicio(posicion)