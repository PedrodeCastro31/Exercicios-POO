import datetime
from typing import List
from quarto import Quarto

class Hospede:
    def __init__(self, nome: str, cpf: str):
        self.nome = nome
        self.cpf = cpf
        self.listaReservas: List["Reserva"] = []

    @property
    def mostraListaReserva(self):
        if len(self.listaReservas) == 0:
            print(f"{self.nome} ainda não realizou nenhuma Reserva.\n")
            return
        msg:str = f"\nLista de Reservas: {self.nome}\n"
        from reserva import Reserva
        for reserva in self.listaReservas:
            reserva: Reserva
            dataEntrada, dataSaida = reserva.datasFormatadas
            if reserva.finalizada == True:
                msg += "Reserva Finalizada"
            else:
                msg += "Reserva Ativa"
            msg += f""
            msg += f"Entrada: {dataEntrada} | Saída: {dataSaida}"
            msg += "\n"
            msg += f"Número do Quarto: {reserva.quarto.numero}\n"
            msg += f"Tipo do Quarto: {reserva.quarto.tipo}\n"
            msg += f"Preço da Diária: R$ {reserva.quarto.precoDiaria}\n"
            msg += "\n"
            msg += f"Valor Total: R$ {reserva.valor_total}"
            msg += f"===========================================\n"
        return msg
    
    def adicionaReserva(self, reserva):
        from reserva import Reserva
        reserva: Reserva
        self.listaReservas.append(reserva)


    