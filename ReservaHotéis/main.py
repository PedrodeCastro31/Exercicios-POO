from datetime import datetime
from hotel import Hotel
from quarto import Quarto
from reserva import Reserva
from hospede import Hospede
import utilitarios


# Um Comentário aqui do código: Apesar deu saber que eu poderia fazer funções, já que a lógica das verificações estão meio complexas e repetitivas, considerando que
# eu não posso so meter um return ou exit(), eu me submeti nesse código a não fazer isso, pra ver como eu me saia com a lógica.
# Arrependi, aumentou muito o tempo!


msgInicial: str = "\nOlá Pedro! Seja bem vindo a mais um Exercício de POO!\n"
msgInicial += "Dessa vez, você é dono de um Hotel e precisa de um sistema para organizar seu estabelecimento!\n"
msgInicial += "\n"

print(msgInicial)
nomeHotel = input("Qual é o Nome do seu Hotel?\n")

msgInicial = "Utilize o comando /AJUDA para tomar conhecimento de nossos comandos!"
print(msgInicial)

msgAjuda: str = "\nNossos Comandos São:\n"
msgAjuda += "\n"
msgAjuda += "/CONSTRUIR, comando para construir um novo quarto!\n"
msgAjuda += "/DEMOLIR, comando para demolir um quarto!\n"
msgAjuda += "/RESERVAR, comando para reservar um quarto!\n"
msgAjuda += "/CHECKOUT, comando para liberar um quarto!\n"
msgAjuda += "/HOSPEDE, comando para mostrar todas as Reservas de um Hóspede!\n"
msgAjuda += "/QUARTO, comando para mostrar informações de um Quarto!\n"
msgAjuda += "/HOTEL, comando que mostra as Informações Gerais do Hotel!\n"
msgAjuda += "/LISTAQUARTOS, comando para exibir todos os quartos do Hotel!\n"
msgAjuda += "/LISTARESERVAS, comando para exibir todos as reservas do Hotel!\n"
msgAjuda += "/SAIR, comando para sair do sistema.\n"
msgAjuda += "\n"

hotel: Hotel = Hotel(nomeHotel)
msgInicial = "\nComando:\n"

while True:
    respostaUsuarioBruta = input(msgInicial)
    respostaUsuario = respostaUsuarioBruta.upper()

    if respostaUsuario == "/AJUDA":
        print("\n")
        print(msgAjuda)

    elif respostaUsuario == "/CONSTRUIR":
        print("\n")       
        numeroQuarto = input("\nQual será o número desse quarto?\n")
        if len(hotel.quartos) == 0:
            tipoQuartoBruto = input("\nQual será o Tipo desse novo quarto?\n'Simples,'\n'Duplo,'\n'Luxo,'\n'Cobertura,'\n'Presidencial.'\n")
            tipoQuarto = tipoQuartoBruto.upper()
            if tipoQuarto != "SIMPLES" and tipoQuarto != "DUPLO" and tipoQuarto != "LUXO" and tipoQuarto != "COBERTURA" and tipoQuarto != "PRESIDENCIAL":
                print(f"O Hotel não possui quartos do tipo {tipoQuarto}!")
            else:
                quarto: Quarto = Quarto(numeroQuarto, tipoQuarto, disponivel=True)
                hotel.construirQuarto(quarto)
        else:
            qtdOperacoes: int = 0
            processofinalizado: bool = False
            for quartoExistente in hotel.quartos:
                quartoExistente: Quarto
                qtdOperacoes += 1
                if quartoExistente.numero != numeroQuarto and processofinalizado == False:
                    if qtdOperacoes == len(hotel.quartos):
                        tipoQuartoBruto = input("\nQual será o Tipo desse novo quarto?\n'Simples,'\n'Duplo,'\n'Luxo,'\n'Cobertura,'\n'Presidencial.'\n\n")
                        tipoQuarto = tipoQuartoBruto.upper()
                        if tipoQuarto != "SIMPLES" and tipoQuarto != "DUPLO" and tipoQuarto != "LUXO" and tipoQuarto != "COBERTURA" and tipoQuarto != "PRESIDENCIAL":
                            print(f"O Hotel não possui quartos do tipo {tipoQuarto}!")
                        else:
                            quarto: Quarto = Quarto(numeroQuarto, tipoQuarto, disponivel=True)
                            hotel.construirQuarto(quarto)
                            processofinalizado = True
                else:
                    if processofinalizado == False:
                        print(f"O Quarto: {quarto.numero}, já existe")

    
    elif respostaUsuario == "/DEMOLIR":
        print("\n")
        if len(hotel.quartos) != 0: 
            numeroQuarto = input("Qual é o Número do Quarto que você deseja Demolir?\n")
            hotel.demolirQuarto(numeroQuarto)
        else: 
            print("Não existe nenhum quarto no Hotel, Ainda!")

    elif respostaUsuario == "/RESERVAR":
        print("\n")
        if len(hotel.quartos) != 0: 
            nomeHospede = input("Qual é o nome do Hóspede que fará a Reserva?\n")
            cpfHospede = input("\nQual é o CPF desse Hóspede?\n")
            cpfValido = utilitarios.validaCPF(cpfHospede)
            if cpfValido == True:
                hospede: Hospede =Hospede(nomeHospede, cpfHospede)
                qtdOperacoes:int = 0 
                if len(hospede.listaReservas) != 0:
                    for reserva in hospede.listaReservas:
                        if reserva.finalizada == True:
                            if qtdOperacoes == len(hospede.listaReservas):                 
                                tipoQuartoBruto = input("\nQual é o tipo de Quarto que o Hóspede quer reservar?\n'Simples,'\n'Duplo,'\n'Luxo,'\n'Cobertura,'\n'Presidencial.'\n\n")
                                tipoQuarto = tipoQuartoBruto.upper()
                                if tipoQuarto == "SIMPLES" or tipoQuarto == "DUPLO" or tipoQuarto == "LUXO" or tipoQuarto == "COBERTURA" or tipoQuarto == "PRESIDENCIAL":
                                        for quartoExistente in hotel.quartos:
                                            quartoExistente: Quarto
                                            if quartoExistente.tipo == tipoQuarto and quartoExistente.disponivel == True:
                                                numeroQuarto = quartoExistente.numero
                                                quarto: Quarto = Quarto(numeroQuarto, tipoQuarto, True)
                                                dataEntradaBruta = input("Qual é a data e Horário de Entrada: dd/mm/aaaa hh:mm\n")
                                                data_entrada: datetime = None
                                                try:
                                                    data_entrada: str = datetime.strptime(dataEntradaBruta, '%d/%m/%Y %H:%M')
                                                except:
                                                    print("A Data não está no formato solicitado")
                                                dataSaidaBruta: str = input("Qual é a data e Horário de Saída: dd/mm/aaaa hh:mm\n")
                                                data_saida: datetime = None
                                                try:
                                                    data_saida = datetime.strptime(dataSaidaBruta, '%d/%m/%Y %H:%M')
                                                except:
                                                    print("A Data não está no formato Solicitado")
                                                reserva: Reserva = Reserva(quarto, hospede, data_entrada, data_saida)
                                                hotel.adicionaReserva(reserva, numeroQuarto)
                                                hotel.adicionaHospede(hospede)
                                                hospede.adicionaReserva(reserva)
                                                print(f"\nQuarto: {numeroQuarto, tipoQuarto} reservado por {nomeHospede}!\n")
                                            else:
                                                qtdOperacoes += 1
                                            if qtdOperacoes == len(hotel.quartos):
                                                print(f"Não Existem quartos do tipo {tipoQuarto} disponíveis no Hotel!")
                                else:
                                    print(f"O Hotel não possui quartos do tipo {tipoQuarto}!")
                            qtdOperacoes += 1 
                        else:
                            print(F"O Hóspede: {nomeHospede} possui reservas Ativas!")
                else:
                    tipoQuartoBruto = input("Qual é o tipo de Quarto que o Hóspede quer reservar?\n'Simples,'\n'Duplo,'\n'Luxo,'\n'Cobertura,'\n'Presidencial.'\n\n")
                    tipoQuarto = tipoQuartoBruto.upper()
                    if tipoQuarto == "SIMPLES" or tipoQuarto == "DUPLO" or tipoQuarto == "LUXO" or tipoQuarto == "COBERTURA" or tipoQuarto == "PRESIDENCIAL":
                            for quartoExistente in hotel.quartos:
                                quartoExistente: Quarto
                                if quartoExistente.tipo == tipoQuarto and quartoExistente.disponivel == True:
                                    numeroQuarto = quartoExistente.numero
                                    quarto: Quarto = Quarto(numeroQuarto, tipoQuarto, True)
                                    dataEntradaBruta = input("Qual é a data e Horário de Entrada: dd/mm/aaaa hh:mm\n")
                                    data_entrada: datetime = None
                                    try:
                                        data_entrada: str = datetime.strptime(dataEntradaBruta, '%d/%m/%Y %H:%M')
                                    except:
                                        print("A Data não está no formato solicitado")
                                    dataSaidaBruta: str = input("Qual é a data e Horário de Saída: dd/mm/aaaa hh:mm\n")
                                    data_saida: datetime = None
                                    try:
                                        data_saida = datetime.strptime(dataSaidaBruta, '%d/%m/%Y %H:%M')
                                    except:
                                        print("A Data não está no formato Solicitado")
                                    reserva: Reserva = Reserva(quarto, hospede, data_entrada, data_saida)
                                    hotel.adicionaReserva(reserva, numeroQuarto)
                                    hotel.adicionaHospede(hospede)
                                    hospede.adicionaReserva(reserva)
                                    print(f"\nQuarto: {numeroQuarto, tipoQuarto} reservado por {nomeHospede}!\n")
                                else:
                                    qtdOperacoes += 1
                                if qtdOperacoes == len(hotel.quartos):
                                    print(f"Não Existem quartos do tipo {tipoQuarto} disponíveis no Hotel!")
                    else:
                        print(f"O Hotel não possui quartos do tipo {tipoQuarto}!")
            else: 
                print("CPF informado de maneira Incorreta")
        else: 
            print("Não Existe nenhum quarto no hotel, Ainda!") 

    elif respostaUsuario == "/CHECKOUT":
        print("\n")
        if len(hotel.hospedes) != 0: 
            nomeHospede = input("Qual é o nome do Hospede que está fazendo Checkout?\n")
            qtdOperacoes: int = 0
            for hospedeExistente in hotel.hospedes:
                if hospedeExistente.nome == nomeHospede:
                    if len(hotel.reserva) != 0:
                        qtdOperacoes = 0
                        for reservaExistente in hotel.reserva:
                            reservaExistente: Reserva
                            if reservaExistente.hospede.nome == nomeHospede and reservaExistente.finalizada == False:
                                reservaExistente.finalizada = True
                                reservaExistente.quarto.liberar()
                            qtdOperacoes += 1
                            if reservaExistente.hospede.nome != nomeHospede and qtdOperacoes == len(hotel.listaReservas):
                                print(f"Nenhuma reserva Ativa foi encontrada em nome de {nomeHospede}")
                    else:
                        print("Nenhum Hóspede fez reservas, Ainda!")
                else:
                    if qtdOperacoes == len(hotel.hospedes):
                        print(f"Hospede {nomeHospede}, nao encontrado!")
                qtdOperacoes += 1
        else: 
            print(f"Nenhum Hóspede no Sistema!")

    elif respostaUsuario == "/HOSPEDE":
        print("\n")
        if len(hotel.hospedes) != 0:
            nomeHospede = input("Qual é o nome do Hóspede que você deseja saber as Reservas?")
            qtdOperacoes: int = 0
            for hospedeExistente in hotel.hospedes:
                if hospedeExistente.nome == nomeHospede:
                    resposta = hospedeExistente.mostraListaReserva()
                    print(resposta)
                qtdOperacoes += 1 
                if qtdOperacoes == len(hotel.hospedes) and hospedeExistente.nome != nomeHospede:
                    print(f"Hóspede: {nomeHospede}, não encontrado!")
        else: 
            print(f"Nenhum Hóspede no Sistema!")
    
    elif respostaUsuario == "/QUARTO":
        print("\n")
        if len(hotel.quartos) != 0:
            numeroQuarto = input("Qual é o Número do Quarto que você deseja ver as informações?")
            qtdOperacoes: int = 0
            for quartoExistente in hotel.quartos:
                if quartoExistente.numero == numeroQuarto:
                    resposta = quartoExistente.__str__()
                    print(resposta)
                qtdOperacoes += 1 
                if qtdOperacoes == len(hotel.quartos) and quartoExistente.numero != numeroQuarto:
                    print(f"Quarto: {numeroQuarto}, não encontrado!")
        else:
            print("Nenhum Quarto foi construído, Ainda!")

    elif respostaUsuario == "/HOTEL":
        print("\n")
        resposta = hotel.__str__()
        print(resposta)

    elif respostaUsuario == "/LISTAQUARTOS":
        print("\n")
        hotel.listaQuarto

    elif respostaUsuario == "/LISTARESERVAS":
        print("\n")
        hotel.listaReservas

    elif respostaUsuario == "/SAIR":
        print("\n")
        break

    else:
        print("\n")
        print("Comando não reconhecido, lembre de utilizar '/' \n")

