class Node:
    def __init__(self, data):
        self.data = data


class Stack:

    def __init__(self, leng):
        self.topo = None
        self.pilha = []
        self.leng = leng

    def push(self, data):

        if len(self.pilha) == self.leng:
            print("Stack is Full")
            return -1

        node = Node(data)
        self.pilha.append(node)
        self.topo = self.pilha[-1]

    def pop(self):
        if self.pilha.__len__() == 0:
            print("Stack is Empty")
            return

        self.pilha = self.pilha[0:-1]
        if self.pilha.__len__() == 0:
            self.topo = None
            return

        self.topo = self.pilha[-1]

    def peek(self):
        if self.topo != None:
            print(self.topo.data)
        else:
            print("Is Empty")
        
    
c = Stack(5)

c.push(1)
c.push(2)
c.push(3)
c.push(4)
c.push(5)

c.peek()

c.pop()
c.pop()
c.pop()
c.pop()
c.pop()
c.pop()


c.peek()
