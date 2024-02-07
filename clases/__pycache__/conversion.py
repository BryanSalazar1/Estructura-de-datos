'''Implementador'''

from Nodo import Nodo
class Implementador(Nodo):
    def __init__(self,val):
        super.__init__(val)
    def a(self):
        e=[1,2,3,4,5]
        head=Nodo()
        Curr=head
        for i in e:
            curr.val=i
            Curr.next=Nodo()
            curr=curr.next
        return head  

    if __name__=="__main__":
      lista= list(range(1,6))
      head=Nodo()
      print(head)
