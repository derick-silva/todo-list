list = [] #criando uma lista vazia


while True:
  try:
    opcao = int(input('''
      Selecione uma opção

      1 Ver Tarefas
      2 Adcionar Tarefa
      3 Remover Tarefa
      4 Sair                                           
                      ''') )
  # Verifica qual foi o valor digitado pelo usuario / Compara se a lista esta vazia
    if opcao == 1:
      if list == []:
        print("Ainda não tem nenhuma tarefa")
        print("Adcione uma com opção 2")

      # Exibe na tela os item da lista usando a estrutura de repetição for e a função enumerate para mostrar tambem os indices 
      else: 
        print("Lista de tarefas")
        for index, item in enumerate(list):
          print(index, item)

  # Adiciona item a lista usando o append()
    elif opcao == 2: 
      tarefa = input("Adcione uma tarefa:  ")
      list.append(tarefa)
      print("Tarefa adiciona com sucesso")
      
  # Compara se lista esta vazia / Remove item pelo indice informado pelo usuario
    elif opcao == 3: 
      if list == []:
        print("Não a tarefas na lista")
        print("***********************")
      else:
        try:
          indice = int(input("Digite o indice do item que deseja remover "))
          list.pop(indice)
          print("Tarefa removida com sucesso")

        except:
          print("O indice informado é inexistente")
          print("Você pode verificar os indices na opção 1")

    else:
      if opcao != 4:
        print("Digite um valor presente nas opções")
      else:
        print("Saindo")
        print('>>>>')
        exit()


  except ValueError:
    print('''
    Valor incorreto! :(
    Este valor não é um numero válido!
    ''')

        
       





