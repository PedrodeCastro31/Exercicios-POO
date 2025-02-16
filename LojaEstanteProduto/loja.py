from typing import List
from estante import Estante 

class Loja:
    def __init__(self, nome):
        self.nome = nome
        self.listaEstantes: List[Estante] = []

    def adicionaEstante(self, estante: Estante):
        for estantesExistentes in self.listaEstantes:
            if estantesExistentes.codigoEstante == estante.codigoEstante:
                print(f"A Estante {estante.codigoEstante}, já existe.")
                return
        self.listaEstantes.append(estante)
        print(f"Estante {estante.codigoEstante} adicionada com Sucesso!")

    
    def removeEstante(self, estante: Estante):
        for estantesExistentes in self.listaEstantes:
            if estantesExistentes.codigoEstante == estante.codigoEstante:
                self.listaEstantes.remove(estante)
            else:
                print(f"Estante {estante.codigoEstante}, não existe na Loja.")
                return
            print(f"Estante {estante.codigoEstante} removida com Sucesso!")
            return
        
    @property
    def exibeInventario(self):
        if len(self.listaEstantes) == 0:
            print("Nenhuma Estante na Loja")
            return
        valorTotalLoja: float = 0.0
        for estante in self.listaEstantes:
            estante: Estante
            valorEstante = estante.valorTotalEstante()
            valorTotalLoja += valorEstante
            print(f"Valor da Estante {estante.codigoEstante}: R$ {valorEstante}")
        print(f"Valor Total da Loja: R$ {valorTotalLoja}")  
        return