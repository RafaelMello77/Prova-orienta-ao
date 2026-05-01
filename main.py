from Controllers.guilda_contoller import *
from Controllers.missao_contoller import *
from Views.view import *
from Models.arquivoddados import criar_tabelas

criar_tabelas()

while True:
    print("\n1 - Registrar heroi")
    print("2 - Listar herois")
    print("3 - Criar missao")
    print("4 - Concluir missao")
    print("0 - Sair")

    op = input("Escolha: ")


    if op == "1":
            nome = input("Nome: ")
            classe = input("Classe: ")
            h = registrar_heroi(nome, classe)
            print("Criado:", h.resumo())

    elif op == "2":
            exibir_herois(listar_herois())

    elif op == "3":
            titulo = input("Titulo: ")
            desc = input("Descricao: ")
            xp = int(input("XP: "))
            hid = int(input("ID heroi: "))
            m = criar_missao(titulo, desc, xp, hid)
            exibir_missao(m)

    elif op == "4":
            mid = int(input("ID missao: "))
            m = concluir_missao(mid)
            if m:
                print("Missao concluida!")

    elif op == "0":
            break
