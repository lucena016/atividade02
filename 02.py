class Animal:
    def __init__(self, nome, idade, especie):
        self.nome = nome
        self.idade = idade
        self.especie = especie

    def emitir_som(self):
        print(f"O {self.especie} {self.nome} está emitindo um som.")

    def mostrar_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Especie: {self.especie}")

# Example usage:
meu_animal = Animal("Fido", 5, "Cachorro")
meu_animal.emitir_som()
meu_animal.mostrar_informacoes()