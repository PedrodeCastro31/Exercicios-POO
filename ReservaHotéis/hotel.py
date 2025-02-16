from typing import List
from hospede import Hospede
from quarto import Quarto
from reserva import Reserva


class Hotel:
    def __init__(self, nome: str):
        self.nome = nome
        self.quartos: List[Quarto] = []
        self.hospedes: List[Hospede] = []
        self.reserva: List[Reserva] = []

    def adicionaHospede(self, hospede: Hospede):
        if len(self.hospedes) != 0:
            for hospedeExistente in self.hospedes:
                if hospedeExistente.nome == hospede.nome:
                    return
        self.hospedes.append(hospede)

    def adicionaReserva(self, reserva: Reserva, numeroQuarto):
        for quarto in self.quartos:
            if quarto.numero == numeroQuarto:
                quarto.reservar()
        self.reserva.append(reserva)

    def construirQuarto(self, quarto: Quarto):
        for quartoExistente in self.quartos:
            quartoExistente: Quarto
            if quartoExistente.numero == quarto.numero:
                print(f"O Quarto {quarto.numero} já existe")
                return
        self.quartos.append(quarto)
        print(f"\nO Quarto {quarto.numero} foi construído com sucesso! Depois você passa O PIX!\n")
        return
    
    def demolirQuarto(self, numeroQuarto: str):
        qtdOperacoes: int = 0
        for quartoExistente in self.quartos:
            quartoExistente: Quarto
            qtdOperacoes += 1
            if quartoExistente.numero == numeroQuarto:
                self.quartos.remove(quartoExistente)
            elif qtdOperacoes == len(self.quartos):
                print(f"O Quarto {numeroQuarto} não existe!")
                return
            print(f"O Quarto {numeroQuarto} foi demolido com sucesso!")
            return

    @property
    def listaQuarto(self):
        msg: str = "Lista dos Quartos no Hotel:\n"
        msg += "\n"
        if len(self.quartos) == 0:
            print("Nenhum quarto foi construído no Hotel, AINDA!") 
            return
        else: 
            for quartoExistente in self.quartos:
                quartoExistente: Quarto
                msg += f"Número do Quarto: {quartoExistente.numero}\n"
                msg += f"Tipo do Quarto: {quartoExistente.tipo}\n"
                msg += f"Preço da Diária: R$ {quartoExistente.precoDiaria}\n"
                if quartoExistente.disponivel == True:
                    msg += f"Quarto Disponível\n"
                else:
                    msg += f"Quarto Reservado\n"
                msg += f"======================================\n"
        print(msg)
        return
    
    @property
    def listaReservas(self):
        msg: str = "Lista das Reservas no Hotel:\n"
        msg += "\n"
        if len(self.quartos) == 0:
            print("Nenhum quarto foi reservado no Hotel, obviamente porque está fora de época!") 
            return
        else: 
            for reservaExistente in self.reserva:
                reservaExistente: Reserva
                dataEntrada, dataSaida = reservaExistente.datasFormatadas
                msg += f"Entrada: {dataEntrada} | Saída: {dataSaida}"
                msg += "\n"
                msg += f"Número do Quarto: {reservaExistente.quarto.numero}\n"
                msg += f"Tipo do Quarto: {reservaExistente.quarto.tipo}\n"
                msg += f"Preço da Diária: R$ {reservaExistente.quarto.precoDiaria}\n"
                msg += "\n"
                msg += f"Nome do Hóspede: {reservaExistente.hospede.nome}\n"
                msg += f"CPF do Hóspede: {reservaExistente.hospede.cpf}\n"
                msg += "\n"
                msg += f"Valor Total: R$ {reservaExistente.valor_total}\n"
                msg += f"===========================================\n"
        print(msg)
        return
    
    def __str__(self):
        retorno: str = f"Nome do Hotel: {self.nome}\n"
        if len(self.quartos) == 0:
            retorno += f"Quantidade de Quartos no Hotel: 0\n"
        else: 
            retorno += f"Quantidade de Quartos no Hotel: [{len(self.quartos)}] \n"
        if len(self.reserva) == 0:
            retorno += f"Quantidade de Reservas já Feitas no Hotel: 0 \n"
        else: 
            retorno += f"Quantidade de Reservas já Feitas no Hotel: [{len(self.reserva)}]\n"
        return retorno


        
