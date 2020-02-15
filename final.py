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
        return print(self.lista)

    def tamanho(self):
        return self.quant

    def pertence(self,valor):    
        return valor in self.lista

    def eh_subconjunto(self,valor,conj):
        if valor.issubset(conj):
            return print("É subconjunto!")
        else:
            return print("Não é subconjunto!")


    
