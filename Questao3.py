tarefas = []

opcao = 0

while opcao != 4:
    print ("\n1 -  Cadastrar Tarefa")
    print ("2 -  Listar Tarefas")
    print ("3 -  Mostrar quantidade de Tarefas")
    print ("4 -  Sair")

    opcao = int(input("Escolha uma opcao: "))

    if opcao == 1:
        tarefa = input("Digite o nome da Tarefa: ")
        tarefas.append(tarefa)

    elif opcao == 2:
        print("Tarefas Cadastradas:")
        for tarefa in tarefas:
            print(tarefa)
    
    elif opcao == 3:
        print("Total de Tarefas:", len(tarefas))
    
    elif opcao == 4:
        print("Programa encerrado.")
    
    else:
        print("Opção inválida")
