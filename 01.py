class Carro:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.ligado = False
        self.velocidade = 0

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print("O carro está ligado.")
        else:
            print("O carro já está ligado.")

    def desligar(self):
        if self.ligado:
            self.ligado = False
            self.velocidade = 0
            print("O carro está desligado.")
        else:
            print("O carro já está desligado.")

    def acelerar(self, incremento):
        if self.ligado:
            self.velocidade += incremento
            print(f"O carro acelerou para {self.velocidade} km/h.")
        else:
            print("O carro precisa estar ligado para acelerar.")

# Exemplo de uso da classe Carro
meu_carro = Carro("Toyota", "Corolla", 2022, "Prata")
print(f"Marca: {meu_carro.marca}, Modelo: {meu_carro.modelo}, Ano: {meu_carro.ano}, Cor: {meu_carro.cor}")

meu_carro.ligar()
meu_carro.acelerar(30)
meu_carro.acelerar(20)
meu_carro.desligar()