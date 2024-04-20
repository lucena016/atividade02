class Estudante:
    def __init__(self, nome, idade, notas):
        self.nome = nome
        self.idade = idade
        self.notas = notas

    def calcular_media(self):
        if self.notas:
            return sum(self.notas) / len(self.notas)
        else:
            return 0

    def verificar_aprovacao(self, media_minima=6.0):
        media = self.calcular_media()
        if media >= media_minima:
            return f'O estudante {self.nome} {self.idade}  foi aprovado com média {media:.2f}.'
        else:
            return f'O estudante {self.nome} {self.idade} foi reprovado com média {media:.2f}.'



estudante1 = Estudante(nome='João', idade=20, notas=[7, 8, 6, 9, 8])
print(estudante1.verificar_aprovacao())  

estudante2 = Estudante(nome='Maria', idade=22,notas=[5, 6, 4, 3, 6])
print(estudante2.verificar_aprovacao())  