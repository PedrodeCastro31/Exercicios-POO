from typing import List, Dict
from livro import Livro

class Biblioteca:
    def __init__(self, nome: str):
        self.nome: str = nome
        self.livros: List[Livro] = []

    def adicionaNovosLivros(self, livro: Livro):
        self.livros.append(livro)
        print(f"Livro: {livro.nome} adicionado com sucesso!")
        return
    
    def indisponibilizaLivros(self, livro: Livro):
        for livroBiblioteca in self.livros:
            if livroBiblioteca.nome.upper() == livro.nome.upper():
                if livroBiblioteca.disponivel:
                    livroBiblioteca.disponivel = False
                    print(f"Livro: {livro.nome} emprestado com sucesso.")
                else:
                    print(f"Livro: {livro.nome} já está emprestado.")
                return
        print(f"Livro: {livro.nome} não encontrado na biblioteca.")

    def disponibilizaLivros(self, livro: Livro):
        for livroBiblioteca in self.livros:
            if livroBiblioteca.nome.upper() == livro.nome.upper():
                if not livroBiblioteca.disponivel:
                    livroBiblioteca.disponivel = True
                    print(f"Livro: {livro.nome} devolvido com sucesso.")
                else:
                    print(f"Livro: {livro.nome} já está disponível.")
                return
        print(f"Livro: {livro.nome} não encontrado na biblioteca.")

        
    def mostraIventario(self):
        if len(self.livros) == 0:
            print("Nenhum livro na biblioteca.")
            return
        for livro in self.livros:
            if livro.disponivel:
                status = "Disponível"
            else:
                status = "Indisponível" 
            print(f"{livro.nome}: {livro.autor}, {status} ")
        print("\n")
        print(f"{len(self.livros)} Livros na {self.nome}.")
        return
    
