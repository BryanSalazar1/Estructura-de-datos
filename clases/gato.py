from objetos import Animal

class Gato(Animal):

    def __init__(self, nombre):
        super().__init__(nombre)

    def maullar(self):
        print("miau") 

if __name__== "__main__":
    perro=Animal("firulais")  
    #perro.maullar()
        

if __name__== "__main__":
    gato = Gato("Michi")
    print(gato)  
    gato.maullar
    
