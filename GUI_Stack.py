import time

# Bem formada: ( ( ) [ ( ) ] )
#Mal formada: (])

class Stack:

    def __init__(self) -> None:
        self.stack = []
        self.topo = None
       

    def push(self, value) -> None:
        self.stack.append(value)
        self.topo = self.stack[-1]

    def isEmpty(self)-> bool:
        return len(self.stack) == 0
    
    def peek(self) -> None:
        if len(self.stack):
            return self.stack[-1]
        
        print("Stack is empty")
        return
        
    def isFull(self):
        pass
        #I'm not implementing is this case

    def pop(self) -> None:
        if len(self.stack):
            self.stack.pop()

        else:
            print("Is empty")
            return 


def analisa(text: str) -> bool:
    pilha = []

    for caractere in text:
        if caractere == "(" or caractere == "[":
            pilha.append(caractere)
        elif caractere == ")" or caractere == "]":
            if not pilha:
                return False
            
            pilha.pop()

        return not pilha

    
str1 = "[()]"
str2 = ")([])"


print(analisa(str1))