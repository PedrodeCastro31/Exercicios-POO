from livro import Livro
from biblioteca import Biblioteca

biblioteca: Biblioteca = Biblioteca("Biblioteca do Pedro")


msgInicial = "Olá, Pedro! Utilize /AJUDA para conhecer os comandos!\n"
msgAjuda = "Nossos comandos são:\n"
msgAjuda += "'/EXPLORAR': Comando para Explorar os livros da nossa Biblioteca.\n"
msgAjuda += "'/ADICIONAR': Comando para adicionar um novo Livro à nossa biblioteca.\n"
msgAjuda += "'/EMPRESTAR': Comando para emprestar um livro da nossa Biblioteca.\n"
msgAjuda += "'/DEVOLVER': Comando para devolver um livro à nossa Biblioteca.\n"
msgAjuda += "'/SAIR': Comando para Sair da Biblioteca.\n"
msgAjuda += "\n"
msgAjuda += "Qualquer dúvida, eu não posso te ajudar, se vira aí."
msgAjuda += "\n"

while True:

    respostaUsuarioBruta = input(msgInicial)
    respostaUsuario = respostaUsuarioBruta.upper()
    if respostaUsuario == "/AJUDA":
        print("\n")
        print(msgAjuda)
    
    if respostaUsuario == "/EXPLORAR":
        print("\n")
        biblioteca.mostraIventario()

    if respostaUsuario == "/ADICIONAR":
        print("\n")
        nomeLivro = input("Qual é o nome do Livro que você quer Adicionar?\n")
        autorLivro = input("Qual é o Autor desse Livro?\n")
        print("\n")
        livro:Livro = Livro(nomeLivro, autorLivro, True)
        biblioteca.adicionaNovosLivros(livro)
    
    if respostaUsuario == "/EMPRESTAR":
        print("\n")
        nomeLivro = input("Qual é o nome do Livro que você deseja Emprestar? Seja exato no nome!\n")
        print("\n")
        livro:Livro = Livro(nomeLivro,"", True)
        biblioteca.indisponibilizaLivros(livro)

    if respostaUsuario == "/DEVOLVER":
        print("\n")
        nomeLivro = input("Qual é o nome do Livro que você deseja Devolver? Seja exato no nome!\n")
        print("\n")
        livro:Livro = Livro(nomeLivro,"", True)
        biblioteca.disponibilizaLivros(livro)

    if respostaUsuario == '/SAIR':
        break

    msgInicial = "\n"
