class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

    def calcular_area(self):
        # Usando a fórmula de Heron para calcular a área de um triângulo
        s = self.calcular_perimetro() / 2
        area = (s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3)) ** 0.5
        return area


# Exemplo de uso da classe Triangulo
triangulo1 = Triangulo(lado1=3, lado2=4, lado3=5)
print("Perímetro:", triangulo1.calcular_perimetro())  # Saída: Perímetro: 12
print("Área:", triangulo1.calcular_area())  # Saída: Área: 6.0
