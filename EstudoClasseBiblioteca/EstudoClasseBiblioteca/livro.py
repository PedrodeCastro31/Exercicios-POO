class Livro:
    def __init__(self, nome:str, autor:str, disponivel:bool):
        self.nome:str = nome
        self.autor:str = autor
        self.disponivel:bool = disponivel

    @property
    def caracteristicasLivro(self):
        return f"Nome do Livro: {self.nome}, Autor do Livro: '{self.autor}'"
    
