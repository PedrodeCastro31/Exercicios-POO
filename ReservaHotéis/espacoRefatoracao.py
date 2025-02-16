import hotel
from quarto import Quarto
from hotel import Hotel

hotel: Hotel = Hotel("Nome")

respostaUsuario = "/CONSTRUIR"

if respostaUsuario == "/CONSTRUIR":
    print("\n")
    numeroQuarto = input("\nQual será o número desse quarto?\n")
    if len(hotel.quartos) != 0:
        for quartoExistente in hotel.quartos:
            quartoExistente: Quarto
            if quartoExistente.numero == numeroQuarto:
                print(f"O Quarto {quarto.numero} já existe")
            else:
                tipoQuartoBruto = input("\nQual será o Tipo desse novo quarto?\n'Simples,'\n'Duplo,'\n'Luxo,'\n'Cobertura,'\n'Presidencial.'\n\n")
                tipoQuarto = tipoQuartoBruto.upper()
                if tipoQuarto != "SIMPLES" and tipoQuarto != "DUPLO" and tipoQuarto != "LUXO" and tipoQuarto != "COBERTURA" and tipoQuarto != "PRESIDENCIAL":
                    print(f"O Hotel não possui quartos do tipo {tipoQuarto}!")
                else:
                    quarto: Quarto = Quarto(numeroQuarto, tipoQuarto, disponivel=True)
                    hotel.construirQuarto(quarto)
        