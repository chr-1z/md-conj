class Conjunto():
    def __init__(self):
        self.lista = []
        self.quant = 0

    def inserir(self,valor):
        if valor in self.lista:
            return print("Já possui!")
        else:
            self.lista.append(valor)
            self.quant += 1
            return self.lista
            
    def imprimir(self):
        print(*self.lista, sep=',')

    def tamanho(self):
        return self.quant

    def pertence(self, valor):
        return valor in self.lista
