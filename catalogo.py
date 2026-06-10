filmes = []

while True:
    print("\n=== CATÁLOGO DE FILMES ===")
    print("1 - Adicionar filme")
    print("2 - Ver filmes")
    print("3 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome do filme: ")

        filme = {
            "nome": nome
        }

        filmes.append(filme)

    elif opcao == "2":
        for filme in filmes:
            print(filme["nome"])

    elif opcao == "3":
        break