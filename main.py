class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None

class FilaEncadeada:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None


    def vazio(self):
        return self.primeiro is None


    def enfileirar(self, data):
        new_node = Nodo(data)
        if self.vazio():
            self.primeiro = self.ultimo = new_node
        else:
            self.ultimo.next = new_node
            self.ultimo = new_node


    def fDupla(self):
        if self.vazio():
            print("Fila vazia! Não é possível remover.")
            return None
        else:
            removed_data = self.primeiro.data
            self.primeiro = self.primeiro.next
            if self.primeiro is None:
                self.ultimo = None
            return removed_data

    def Exibir(self):
        if self.vazio():
            print("Fila vazia!")
        else:
            current = self.primeiro
            while current:
                print(current.data, end=" -> ")
                current = current.next
            print("None")


fila = FilaEncadeada()

fila.enfileirar(10)
fila.enfileirar(20)
fila.enfileirar(30)
fila.enfileirar(40)

print("Fila após inserção de elementos:")
fila. Exibir()

print(f"\nElemento removido: {fila.fDupla()}")
print(f"Elemento removido: {fila.fDupla()}")

print("\nFila após remoções:")
fila.Exibir()

fila.enfileirar(50)

print("\nFila final:")
fila. Exibir()
