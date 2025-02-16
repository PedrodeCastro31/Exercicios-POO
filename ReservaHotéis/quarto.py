class Quarto:
    def __init__(self, numero:int, tipo:str, disponivel: bool=True ):
        self.numero = numero
        self.tipo = tipo
        self.precoDiaria = self.precoQuarto(tipo)
        self.disponivel = disponivel

    @property
    def reservar(self):
        if self.disponivel == False:
            print(f"O Quarto: {self.numero}, já está reservado!")
            return
        else:
            self.disponivel = False
            print(f"O Quarto: {self.numero}, foi reservado com sucesso!")
        return
    
    @property
    def liberar(self):
        if self.disponivel == True:
            print(f"O Quarto: {self.numero}, já está liberado!")
            return
        else:
            self.disponivel = True
            print(f"O Quarto {self.numero} foi Liberado com sucesso!")
        return
    
    def precoQuarto(self, tipoBruto: str):
        tipo: str = tipoBruto.upper()
        precoDiaria: float = 0.0
        if tipo == "SIMPLES":
            precoDiaria = 90.0
        elif tipo == "DUPLO":
            precoDiaria = 170.0
        elif tipo == "LUXO":
            precoDiaria = 300.0
        elif tipo == "COBERTURA":
            precoDiaria = 600.0
        elif tipo == "PRESIDENCIAL":
            precoDiaria = 1000.0
        else:
            print(f"O Hotel não possui quartos do tipo {tipo}!")
        return precoDiaria

    def __str__(self):
        retorno: str = ''
        if self.numero is not None and self.numero != 0:
            retorno += f'* Número do Quarto: {self.numero}'
        else:
            retorno += '* Número do Quarto: None'
        if self.tipo is not None and self.tipo != "":
            retorno += f"* Tipo do Quarto: {self.tipo}"
        else: 
            retorno += "* Tipo do Quarto: None"
        if self.precoDiaria is not None and self.precoDiaria != 0.0:
            retorno += f"* Preço Diária: {self.precoDiaria}"
        else:
            retorno += "* Preço Diária: None"
        if self.disponivel == True:
            retorno += "* Quarto Disponível"
        else:
            retorno += "* Quarto Reservado"
        return retorno


            
        
        