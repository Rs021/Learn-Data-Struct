import time

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinked:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            self.tail = new_node    
            return 

        current_node = self.head

        aux = self.tail
        self.tail = new_node
        aux.next = self.tail
        self.tail.prev = aux

        return

        
        

    def display(self):
        current_node = self.head
        while current_node != None:
            print(current_node.data)
            current_node = current_node.next
        return


    def insert_begin(self, data):
        new_node = Node(data)

        aux = self.head

        self.head = new_node
        self.head.next = aux 

        return

class SingleNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinked:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        new_node = SingleNode(data)
        
        if self.head == None:
            self.head = new_node
            return 

        current_node = self.head

        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node
        return


if __name__ == "__main__":
    
    list_test = DoubleLinked()

   
    start = time.time()
    for i in range(1000000):
        list_test.append(i)

    stop = time.time()

    total = stop - start
    print(f"Tempo Total: {total:.2f}")