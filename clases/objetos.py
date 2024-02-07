class Animal:
    def __init__(self,nombre):
        self.nombre=nombre
        self.edad=0
        self.color=""

    def __str__(self) -> str:
        return f"me llamo {self.nombre}"
       # return "me llamo"+ self.nombre
    
    if __name__=="__main__":
        print("Este modulo no esta pensado para ejecucion por si mismo")

        
