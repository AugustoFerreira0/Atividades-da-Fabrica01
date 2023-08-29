pilha_de_tarefas = []

while True:
    print("\nDIGITE O QUE FAZER:")
    print("1. Adicionar tarefa")
    print("2. Executar pilha de tarefas")
    print("3. Sair")
    
    opcao = int(input("\nEscolha uma opção: "))
    
    if opcao == 1:
        descricao_tarefa = input("Digite a descrição da tarefa: ")
        pilha_de_tarefas.append(descricao_tarefa)
        print("Tarefa adicionada à pilha.")
    elif opcao == 2:
        if len(pilha_de_tarefas) == 0:
            print("A pilha de tarefas está vazia.")
        else:
            print("Executando pilha de tarefas:")
            while pilha_de_tarefas:
                tarefa = pilha_de_tarefas.pop()  
                print(f"Executando: {tarefa}")
    elif opcao == 3:
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Escolha novamente.")