class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = 0

    def frear(self):
        print("Veículo freou.")

    def acelerar(self, velocidade):
        self.velocidade += velocidade
        print(f"Veículo acelerou para {self.velocidade} km/h.")


class Carro(Veiculo):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self.cor = cor

    def abrir_porta(self):
        print("Porta aberta.")



meu_carro = Carro("Ford", "Fiesta", "vermelho")
print(f"Marca: {meu_carro.marca}, Modelo: {meu_carro.modelo}, Cor: {meu_carro.cor}")
meu_carro.acelerar(40)
meu_carro.frear()
meu_carro.abrir_porta()


class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = 0

    def frear(self):
        print("Veículo freou.")

    def acelerar(self, velocidade):
        self.velocidade += velocidade
        print(f"Veículo acelerou para {self.velocidade} km/h.")


class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada

    def empinar(self):
        print("A moto empinou!")


minha_moto = Moto("Honda", "CBR600RR", "600cc")
print(f"Marca: {minha_moto.marca}, Modelo: {minha_moto.modelo}, Cilindrada: {minha_moto.cilindrada}")
minha_moto.acelerar(30)
minha_moto.empinar()