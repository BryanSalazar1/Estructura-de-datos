      
    # se hara las operacion correspondientes y se almacena en una variable "r" la cual con .append se agregara al final de la lista susesivamente hasta que la condicion sea falsa y deje de llamarce la funcion a si misma
def fib(num, a, b, x, list):
    r = a + b
    list.append(r)
    a = b
    b = r
    x += 1
    if x < num:
        fib(num, a, b, x, list)
    

# PRINCIPAL--
        #aqui de definen variables tambien se asigna un rango de numeros que se mostraran
print("Escribe un rango")
num = int(input())
a = 0
b = 1
x = 1
# creamos una lista y agreagamos los primeros 2 valores a la lista que es el inicio de la serie 0 y 1
list = [a, b]

# se mandan los datos a la funcion
fib(num, a, b, x, list)
print(list)

   
