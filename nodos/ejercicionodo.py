class Nodo:
    def __init__(self):
        self.val = None
        self.next = None

def Lista():
    e = [1, 2, 3, 4, 5, 6, 7] 

    head = Nodo()
    curr = head

    for i in e:
        curr.val = i
        curr.next = Nodo()
        curr = curr.next

    return head

print("Lista de nodos:")
head = Lista()
curr = head
while curr is not None:
    print(curr.val)
    curr = curr.next

