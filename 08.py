class Retangulo:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def calcular_area(self):
        return self.altura * self.largura

    def calcular_perimetro(self):
        return 2 * (self.altura + self.largura)


# Exemplo de uso da classe Retangulo
retangulo1 = Retangulo(altura=5, largura=10)
print("Área do retângulo:", retangulo1.calcular_area())  # Saída: Área do retângulo: 50
print("Perímetro do retângulo:", retangulo1.calcular_perimetro())  # Saída: Perímetro do retângulo: 30
