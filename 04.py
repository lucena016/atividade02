class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def atualizar_estoque(self, quantidade):
        self.estoque += quantidade
        if quantidade > 0:
            print(f'Estoque atualizado: +{quantidade} unidades de {self.nome}.')
        else:
            print(f'Estoque atualizado: {quantidade} unidades de {self.nome} vendidas.')

    def calcular_preco_total(self, quantidade):
        if quantidade <= self.estoque:
            preco_total = quantidade * self.preco
            print(f'Preço total para {quantidade} unidades de {self.nome}: R${preco_total:.2f}')
        else:
            print(f'Quantidade solicitada de {self.nome} não disponível em estoque.')


produto1 = Produto(nome='Camiseta', preco=25.00, estoque=50)
produto1.atualizar_estoque(10) 
produto1.calcular_preco_total(5)  

produto1.atualizar_estoque(-3)  
produto1.calcular_preco_total(8)  

produto1.atualizar_estoque(-50) 
produto1.calcular_preco_total(20)  