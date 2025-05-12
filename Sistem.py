clientes = {}  

def Menu():
    while True:
        print("\nMenu")
        print("1. Cadastrar Cliente")
        print("2. Deposito")
        print("3. Saque")
        print("4. Transferência")
        print("5. Extrato")
        print("6. Sair")

        options = input("Digite qual opção deseja: ")

        if options == "1":
            print("Cadastro de Cliente")
            nome = input("Digite seu nome: ")
            cpf = input("Digite seu CPF: ")
            saldo_inicial = float(input("Digite seu saldo inicial: "))
            clientes[cpf] = {"nome": nome, "saldo": saldo_inicial, "movimentacoes": []}

        elif options == "2":
            cpf = input("Digite seu CPF: ")
            if cpf in clientes:
                deposito = float(input("Digite o valor que deseja depositar na conta: "))
                clientes[cpf]["saldo"] += deposito
                clientes[cpf]["movimentacoes"].append(f"Depósito: R${deposito}")
            else:
                print("Cliente não encontrado.")

        elif options == "3":
            cpf = input("Digite seu CPF: ")
            if cpf in clientes:
                saque = float(input("Digite o valor que deseja sacar: "))
                if saque <= clientes[cpf]["saldo"]:
                    clientes[cpf]["saldo"] -= saque
                    clientes[cpf]["movimentacoes"].append(f"Saque: R${saque}")
                else:
                    print("Saldo insuficiente.")
            else:
                print("Cliente não encontrado.")

        elif options == "4":
            cpf_origem = input("Digite o CPF da conta de origem: ")
            cpf_destino = input("Digite o CPF da conta de destino: ")
            if cpf_origem in clientes and cpf_destino in clientes:
                valor_transferencia = float(input("Digite o valor da transferência: "))
                if valor_transferencia <= clientes[cpf_origem]["saldo"]:
                    clientes[cpf_origem]["saldo"] -= valor_transferencia
                    clientes[cpf_destino]["saldo"] += valor_transferencia
                    clientes[cpf_origem]["movimentacoes"].append(f"Transferência para {cpf_destino}: R${valor_transferencia}")
                    clientes[cpf_destino]["movimentacoes"].append(f"Transferência de {cpf_origem}: R${valor_transferencia}")
                else:
                    print("Saldo insuficiente para transferência.")
            else:
                print("Uma das contas não foi encontrada.")

        elif options == "5":
            cpf = input("Digite seu CPF para consultar o extrato: ")
            if cpf in clientes:
                print(f"Extrato de {clientes[cpf]['nome']}:")
                for transacao in clientes[cpf]["movimentacoes"]:
                    print(transacao)
                print(f"Saldo atual: R${clientes[cpf]['saldo']}")
            else:
                print("Cliente não encontrado.")

        elif options == "6":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")


Menu()
