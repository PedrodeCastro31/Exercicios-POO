from typing import List
from produto import Produto

class Estante:
    def __init__(self, codigoEstante: str):
        self.codigoEstante = codigoEstante
        self.inventarioEstante: List[Produto] = []
        self.valorTotal: float = 0.0

    def valorTotalEstante(self):
        if len(self.inventarioEstante) == 0:
            return 0.0
        valorTotalEstante: float = 0.0
        for produto in self.inventarioEstante:
            produto: Produto
            valorTotalEstante += produto.quantidade * produto.preco
        return valorTotalEstante

    @property
    def exibeInventario(self):
        if len(self.inventarioEstante) == 0:
            print("Nenhum produto na Estante")
            return
        for produto in self.inventarioEstante:
            produto: Produto
            print(f"Produto: {produto.nome}, Quantidade: {produto.quantidade}, Valor em Estoque: {produto.quantidade * produto.preco}, Código: {produto.codigo}")
        valorEstante = self.valorTotalEstante()
        print(f"Valor Total da Estante: R$ {valorEstante:.2f}")
        return

    def adicionaProduto(self, produto: Produto):
        for produtoInventario in self.inventarioEstante:
            if produto.nome == produtoInventario.nome or produto.codigo == produtoInventario.codigo:
                produtoInventario.quantidade += produto.quantidade
                print(f"{produto.quantidade} {produto.nome} adicionado(s) com sucesso.")
                return
        self.inventarioEstante.append(produto)
        print(f"{produto.quantidade} {produto.nome} adicionado(s) com sucesso.")


    def removeProduto(self, produto: Produto):
        for produtoInventario in self.inventarioEstante:
            if produto.nome == produtoInventario.nome or produto.codigo == produtoInventario.codigo:
                if produtoInventario.quantidade >= produto.quantidade:
                    produtoInventario.quantidade -= produto.quantidade
                    if produtoInventario.quantidade == 0:
                        self.inventarioEstante.remove(produtoInventario)
                    print(f"{produto.quantidade} {produto.nome} removido(s) com sucesso.")
                    return
                else:
                    print(f"Você está tentando vender mais produtos do que temos!")
                    return
        print(f"O Produto {produto.nome} não foi encontrado na estante.")

        