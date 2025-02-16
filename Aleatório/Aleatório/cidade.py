from estado import Estado


class Cidade:
    def __init__(self, nome, estado: Estado):
        self.nome = nome
        self.estado = estado

    def exibeInformacaoCidade(self):
        print(self.nome)
        print(self.estado.nome)
        print(self.estado.abreviacao)


