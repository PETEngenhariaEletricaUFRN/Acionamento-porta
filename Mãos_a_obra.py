"Sistema de Cadastro de Petianos"


petianos = dict()  # Dicionário python


def add_petiano(n, s):
    petianos.update({n: s})  # Atualizar dicionario


resp = 0

while resp != "4":
    print("-=" * 20)
    print("[1] Cadastrar Petiano")  ##Solicitar uma senha para executar esta ação
    print("[2] Excluir Petiano")  ## ''   Solicitar senha
    print("[3] Voltar")

    resp = input("Opção: ")

    if resp == "1":
        nome = input("Nome do Petiano: ")
        senha = input("Senha do Petiano: ")  # colocar asteriscos
        add_petiano(nome, senha)
    elif resp == "2":
        expetiano = input("Digite o nome do Ex-Petiano:")
        del petianos[int(expetiano)]
    elif resp == "3":
        print("Programa finalizado")
    elif resp == "4":
        print(petianos)
        break

        ##Voltar o programa ao inicio
        ##Armazenar em arquivo
