# En las Linked Lists, no asignamos la dirección de memoria en la que se almacena cada elemento, sino
# que asignamos la relación entre posiciones de memoria. 
class Node:
    def __init__(self,data):
        self.data = data        # Inicializado por el usuario
        self.next = None        # Inicializado por defecto en "None"
                                # Debería tomar valores como objeto "Node"

class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    # ------------ Mi código -----------
    def insert(self,head,data):
        # head es un objeto Node
        # data es un dato cualquiera
        
        newNode = Node(data)
        
        # Previo a la inicialización de la lista, head no es un objeto, sino que es "None"
        if head is None:                        # Primera iteración: head viene definido como None
            head = newNode                      # Asignar valor de datos a head
            return head                         # Como es el primer elemento, no hay nada más que hacer.

        current = head                          # Posición actual = posición inicial
        
        while current.next is not None:         # Cuando lleguemos a la posición None, termina el loop
            current = current.next              # Posición actual = próxima posición
        current.next = newNode                  # Cuando llegamos al final (current.next == None), cambiar el valor de None a newNode
        
        return head
    # ------------ ----------------------

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head);


# pruebas.....
# aux = Solution()
# head = aux.insert(None,14)
# head = aux.insert(head,18)
# head = aux.insert(head,200)


# aux.display(head)
# print("")
