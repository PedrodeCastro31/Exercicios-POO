from typing import List
from estado import Estado
from cidade import Cidade
import listaMunicipios 

listadosMunicipios: List[str] = listaMunicipios.concatenaLista(listaMunicipios.listaMunicipiosMG, listaMunicipios.listaMunicipiosMG2)
estado: Estado = Estado("Minas Gerais", "MG")
for municipio in listadosMunicipios:
    cidade: Cidade = Cidade(municipio, estado)
    cidade.exibeInformacaoCidade()
