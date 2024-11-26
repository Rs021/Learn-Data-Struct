class Node:
    def __init__(self, nome: str, turma: str) -> None:
        self.turma = turma
        self.nome = nome


class Fila:
    
    def __init__(self) -> None:
        self.fila = []
        self.fim = 0
    
    def mostra_fila(self)-> None:
        for i in self.fila:
            print(i.nome, i.turma, sep=" ")

    def desinfileira(self):
        del self.fila[0]
        self.fim -= 1

    def enfilherar(self, nome: str, turma: int) -> None:

        if self.fim == 100:
            return False
        
        node = Node(nome, turma)

        self.fila.append(node)

        self.fim += 1

        return True

f = Fila()

ret = f.enfilherar("Ryan", 2001)
ret = f.enfilherar("Lucas", 2001)
ret = f.enfilherar("Felipe", 2001)
ret = f.enfilherar("Marcos", 2001)

ret = f.enfilherar("Joana", 2001)
ret = f.enfilherar("Luana", 2001)
ret = f.enfilherar("Maicon", 2001)

f.desinfileira()
f.desinfileira()

f.mostra_fila()