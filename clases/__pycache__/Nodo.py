'''Modulo contenedor de clase Nodo para listas ligadas'''

class Nodo:
    '''Clase de Nodo'''
    def __init__(self,val):
        '''Inicializador de clase'''
        self.val= val
        self.next=None
    def __str__(self) -> str:
        if self.val:
             return f"valor del nodo={self.val}"  
        return f"el nodo"
         
