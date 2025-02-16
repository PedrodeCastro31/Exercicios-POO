from typing import List

listaMunicipiosMG: List[str] = [
    "Contagem",
    "Belo Horizonte",
    "Nova Lima",
    "Wenceslau Braz"
]

listaMunicipiosMG2: List[str] = [
    "Diamantina",
    "Tiradentes",
    "Ouro Preto",
    "Mariana"
]

def concatenaLista(lista1, lista2):
    listaMunicipios: List[str] = lista1 + lista2
    return listaMunicipios
