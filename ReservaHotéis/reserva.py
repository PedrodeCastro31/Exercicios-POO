from datetime import datetime, timedelta
from hospede import Hospede
from quarto import Quarto

class Reserva:
    def __init__(self, quarto: Quarto, hospede: Hospede, data_entrada: datetime, data_saida: datetime):
        self.quarto = quarto
        self.hospede = hospede
        self.data_entrada = data_entrada
        self.data_saida = data_saida
        self.valor_total: float = self.valorTotal
        self.finalizada: bool = False

    @property
    def valorTotal(self):
        duracao: timedelta = self.data_saida - self.data_entrada
        if duracao.days == 0:
           valor_total = self.quarto.precoDiaria 
        else: 
            valor_total = self.quarto.precoDiaria * duracao.days
        return valor_total
    
    @property
    def datasFormatadas(self) -> tuple:
        entrada_Formatada = datetime.strftime(self.data_entrada,"%d/%m/%Y %H:%M")
        saida_formatada = datetime.strftime(self.data_saida,"%d/%m/%Y %H:%M")
        return entrada_Formatada, saida_formatada
