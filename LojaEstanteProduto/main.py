from loja import Loja
from estante import Estante
from produto import Produto

msgInicial: str = "Olá Pedro! Seja bem vindo a mais um dos exercícios de classe!\n"
msgInicial += "Dessa vez, o exercício  é sobre uma loja, onde você pode adicionar produtos m estntes e estantes na loja!\n"
msgInicial += "\n"



msgAjuda: str = "Nossos comandos são:\n"
msgAjuda += "/CRIAR, Comando que cria um produto ou uma estante para ser adicionado na Loja.\n"
msgAjuda += "/INVENTARIO, Comando que mostra o Inventário de toda a Loja ou de uma Estante específica.\n"
msgAjuda += "/VENDER, Comando que retira o produto da prateleira para ser vendido?\n"


loja: Loja = Loja("Loja de Conveniências do Pedro")

while True:

    print(f"{msgInicial}")
    msgInicial = "\n"

    mensagemUsuarioBruta = input("Use o Comando /Ajuda para aprender os comandos\n")
    mensagemUsuario = mensagemUsuarioBruta.upper()

    if mensagemUsuario == '/AJUDA':
        print(msgAjuda)

    if mensagemUsuario == '/CRIAR':
        mensagemUsuarioBruta = input("Você deseja criar uma 'Estante' ou um 'Produto'?") 
        mensagemUsuario = mensagemUsuarioBruta.upper()
        if mensagemUsuario == 'ESTANTE':
            codigoEstante = input(f"Qual é o Código dessa estante?")
            estante: Estante = Estante(codigoEstante)
            loja.adicionaEstante(estante)
        
        if mensagemUsuario == 'PRODUTO':
            if len(loja.listaEstantes) > 0:
                nomeProduto = input("Qual é o nome do Produto que você quer adicionar?")
                precoProduto = input("Qual é o preço desse produto?")
                codigoProduto = input("Qual é o código desse produto?")
                codigoEstante = input("Qual é o código da Estante onde vocÊ vai colocar o Produto?")
                quantidadeProduto = input("E qual é a quantidade que você deseja colocar na estante")
                produto: Produto = Produto(nomeProduto, quantidadeProduto, precoProduto, codigoProduto)
                for estante in loja.listaEstantes:
                    if estante.codigoEstante == codigoEstante:
                        estante.adicionaProduto(produto)
                    else: 
                        print(f" O código de Estante {codigoEstante} não foi encontrado na lista de Estantes")
            else:
                print("Não existe nenhuma estante ainda na loja, você não pode deixar os produtos no chão!!!")

    if mensagemUsuario == '/INVENTARIO':
        mensagemUsuarioBruta = input("Você deseja olhar o Inventário da 'Loja' ou de uma 'Estante'") 
        mensagemUsuario = mensagemUsuarioBruta.upper()

        if mensagemUsuario == 'LOJA':
            loja.exibeInventario()

        if mensagemUsuario == 'ESTANTE':
            if len(loja.listaEstantes) > 0:   
                codigoEstante = input("Qual é o código da Estante que você quer ver o Inventário?")
                for estanteLoja in loja.listaEstantes:
                    if estanteLoja.codigoEstante == codigoEstante:
                        estanteLoja.exibeInventario()

    if mensagemUsuario == '/VENDER':
        if len(loja.listaEstantes) > 0:   
            mensagemUsuarioBruta = input("Você deseja passar o 'Nome' ou 'Codigo' do Produto?")
            mensagemUsuario = mensagemUsuarioBruta.upper()
            if mensagemUsuario == 'NOME':
                nomeProduto = input("Qual é o Nome do produto que você quer vender?")
            if mensagemUsuario == 'CODIGO':
                codigoProduto = input("Qual é o Código do produto que vocÊ quer vender?")
            for estanteLoja in loja.listaEstantes:
                for produtoEstante in estante.inventarioEstante:
                    if produtoEstante.nome == nomeProduto or produtoEstante.codigo == nomeProduto:
                        quantidadeProduto = input("E qual é a quantidade que você deseja vender desse produto?")
                        if mensagemUsuario == 'NOME':
                            produto: Produto = Produto(nomeProduto, quantidadeProduto, produtoEstante.preco, produtoEstante.codigo)
                        elif mensagemUsuario == 'CODIGO':
                            produto: Produto = Produto(produtoEstante.nome, quantidadeProduto, produtoEstante.preco, codigoProduto)
                        estante.removeProduto(produto)
                    else:
                        print(f"O Produto {nomeProduto}, não foi encontrado")     
        else:
            print("Não existe nenhuma estante ainda na loja, ta tentando enganar o consumidor?")




