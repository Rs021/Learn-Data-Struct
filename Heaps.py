class MinHeap:

    def __init__(self) -> None:
        self.lista = []

    def pai(self, i):
        return (i - 1) // 2
    
    def filho_esq(self, i):
        return (i * 2) + 1
    
    def filho_dir(self, i):
        return (i * 2) + 2
    
    def heapfy(self, lista: list)-> None:
        for i in lista:
            self.insert(i)



    def insert(self, value):
        self.lista.append(value)
        self._heapfy_up(len(self.lista) - 1)
    def _heapfy_up(self, index):

        while index > 0 and self.lista[index] < self.lista[self.pai(index)]:
           self.lista[index], self.lista[self.pai(index)] = self.lista[self.pai(index)], self.lista[index]

           index= self.pai(index)

    def search(self, value, index=0):

        if index >= len(self.lista):
            return 0

        if self.lista[index] == value:
            return index
        
        l =  self.search(value, self.filho_esq(index))
        
        if l != 0:
            return l
        
        return self.search(value, self.filho_dir(index))
    
    def minimun(self):
        if len(self.lista) == 0:
            raise IndexError("Is Empty")
        if len(self.lista) == 1:
            return self.lista.pop()
        
        raiz = self.lista[0]
        self.lista[0] = self.lista.pop()
        self._heapfy_down(0)
        return raiz

    def _heapfy_down(self, index):  
        small = index
        l = self.filho_esq(index)
        r = self.filho_dir(index)

        if l < len(self.lista) and self.lista[l] < self.lista[small]:
            small = l

        if r < len(self.lista) and self.lista[r] < self.lista[small]:
            small = r

        if small != index:
            self.lista[index], self.lista[small] = self.lista[small], self.lista[index]
            self._heapfy_down(small)
    def peek(self):
        if len(self.lista) == 0:
            raise IndexError("Is empty")
        
        return self.lista[0]
        
class MaxHeap:

    def __init__(self) -> None:
        self.lista = []

    def pai(self, i):
        return (i - 1) // 2
    
    def filho_esq(self, i):
        return (i * 2) + 1
    
    def filho_dir(self, i):
        return (i * 2) + 2
    
    def insert(self, value):
        self.lista.append(value) # insere o valor na lista
        self._heapfy_up(len(self.lista) - 1) # chama heapfy_up com o tamanho da lista - 1

    def _heapfy_up(self, index):

        while index > 0 and self.lista[index] > self.lista[self.pai(index)]:
            self.lista[index], self.lista[self.pai(index)] = self.lista[self.pai(index)], self.lista[index]
            #se o numero inserido for maior que o pai então troca de valor

            index= self.pai(index)# atualiza o index até chegar na raiz

    def maximun(self):

        if len(self.lista) == 0: # se a lista estiver vazia retorna um error
            raise IndexError("Is Empty")
        
        if len(self.lista) == 1: # se a lista tiver apenas 1 elementos, remove e retorna 
            return self.lista.pop()
        
        raiz = self.lista[0] # cria um variavel com o valor raiz
        self.lista[0] = self.lista.pop() # remove esse elemento do index 0
        self._heapfy_down(0) # substitui o nó pelo ultimo nó do ultimo nivel
        return raiz # retorna a raiz

    def _heapfy_down(self, index):  

        small = index
        l = self.filho_esq(index)
        r = self.filho_dir(index)


        if l < len(self.lista) and self.lista[l] > self.lista[small]:
            small = l
            # se o filho a esquerdar for maior que o index
            # Então troca o index
        if r < len(self.lista) and self.lista[r] > self.lista[small]:
            small = r
            # se o filho a direita for maior que o index
            # Então troca o index

        if small != index: # caso base da recursão, enquanto small != 0 
            self.lista[index], self.lista[small] = self.lista[small], self.lista[index]
            #troca de valor de index por small

            self._heapfy_down(small) # recursão passando index de small

    def peek(self):

        if len(self.lista) == 0:
            raise IndexError("Is empty")
        
        return self.lista[0]
    
    def search(self, value, index=0):

        if index >= len(self.lista):
            return 0

        if self.lista[index] == value:
            return index
        
        l =  self.search(value, self.filho_esq(index))
        
        if l != 0:
            return l
        
        return self.search(value, self.filho_dir(index))


heap = MinHeap()

lista = [8,3,6,7,89,2,34,56]

heap.heapfy(lista)

print(heap.peek())