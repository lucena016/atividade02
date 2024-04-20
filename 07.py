class Livro:
    def __init__(self, titulo, autor, num_paginas):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas

    def mostrar_informacoes(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Número de páginas: {self.num_paginas}")

    def calcular_palavras_por_pagina(self, num_palavras):
        if self.num_paginas > 0:
            return num_palavras / self.num_paginas
        else:
            return 0


# Exemplo de uso da classe Livro
livro1 = Livro(titulo="Dom Casmurro", autor="Machado de Assis", num_paginas=200)
livro1.mostrar_informacoes()
print("Palavras por página:", livro1.calcular_palavras_por_pagina(50000))  # Assumindo em média 250 palavras por página
