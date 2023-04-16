class Pilha:
    def __init__(self):
        self.items = []

    def esta_vazia(self):
        return self.items == []

    def tamanho(self):
        return len(self.items)

    def top(self):
        if not self.esta_vazia():
            return self.items[-1]

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.esta_vazia():
            return self.items.pop()

pilha = Pilha()

print(pilha.esta_vazia())

pilha.push(1)
pilha.push(2)
pilha.push(3)

print(pilha.top())

print(pilha.tamanho())

print(pilha.pop())

print(pilha.top())

print(pilha.tamanho()) 
