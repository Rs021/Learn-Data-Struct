class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        new_node = Node(data)
        
        if self.head == None:
            self.head = new_node
            return 

        current_node = self.head

        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node
        return

    def to_list(self):
        lista = []

        current_node = self.head

        while current_node != None:
            lista.append(current_node.data)
            current_node = current_node.next

        return lista
        
my_link = Linked()

my_link.append(1)
my_link.append(3)
my_link.append(4)
my_link.append(5)
my_link.append(5)
my_link.append(5)

print(my_link.to_list())