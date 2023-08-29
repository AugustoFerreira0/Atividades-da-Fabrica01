fila_de_tarefas = []

while True:
    print("\nDIGITE O QUE FAZER:")
    print("1. Adicionar tarefa")
    print("2. Executar fila de tarefas")
    print("3. Sair")
    
    opcao = int(input("\nEscolha uma opção: "))
    
    if opcao == 1:
        descricao_tarefa = input("Digite a descrição da tarefa: ")
        fila_de_tarefas.append(descricao_tarefa)
        print("Tarefa adicionada à fila.")
    elif opcao == 2:
        if len(fila_de_tarefas) == 0:
            print("A fila de tarefas está vazia.")
        else:
            print("Executando fila de tarefas:")
            for tarefa in fila_de_tarefas:
                print(f"Executando: {tarefa}")
            fila_de_tarefas = [] 
    elif opcao == 3:
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Escolha novamente.")