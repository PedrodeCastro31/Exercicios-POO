def adição(valor1: float, valor2: float):
    resultado = valor1 + valor2
    return resultado

def subtração(valor1: float, valor2: float):
    resultado = valor1 - valor2
    return resultado

#Tratar multiplicações por números menores do que 1
def multiplicação(valor1: float, valor2: float):
    resultado: float = 0 
    for i in range(valor2):
        resultado += valor1
    return resultado

def divisão(valor1: float, valor2: float):
    resultado: float = 0 
    IndicedaVirgula = 1
    valor1_AUX: float = 0
    while valor1 != 0:
        valor1_AUX: float = valor1
        valor1 -= valor2
        if valor1 - valor2 < 0 :
            for i in range(10):
                valor1 = valor1 + valor1_AUX
            IndicedaVirgula = multiplicação(IndicedaVirgula, 0.1)
        resultado += IndicedaVirgula
    return resultado

def trunca(valor: float):
    pass

def resto(valor: float):
    pass

def numeroDeCasas(valor: float, decimal: bool = False):
    numerodecasas = 1
    resultado:int = 0
    if decimal == False:
        while valor > 1:
            resultado = 0
            while valor != 0:
                valor -= 10
                resultado += 1
            valor = resultado
            numerodecasas +=1
    elif decimal == True:
        pass
    return numerodecasas
            

teste = multiplicação(10, 10)
teste1 = numeroDeCasas(100)
print(teste1)

# // = trunca
# % = resto 