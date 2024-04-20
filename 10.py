class Pedido:
    def __init__(self):
        self.itens = []
        self.total = 0
        self.status = "Pendente"

    def adicionar_item(self, item, preco):
        self.itens.append((item, preco))
        self.total += preco

    def calcular_total(self):
        return self.total

    def alterar_status(self, novo_status):
        self.status = novo_status



pedido1 = Pedido()
pedido1.adicionar_item("Hambúrguer", 10.00)
pedido1.adicionar_item("Batata frita", 5.00)

print("Itens do pedido:")
for item, preco in pedido1.itens:
    print(f"- {item}: R${preco:.2f}")

print("Total a ser pago:", pedido1.calcular_total())  

pedido1.alterar_status("Em preparo")
print("Status do pedido:", pedido1.status)  
