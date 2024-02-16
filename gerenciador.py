import os


tarefa = []

def add_task():
  os.system("clear")

  tarefa.append(input("\nAdicionar tarefa: "))
  print("\nTarefa adicionada!")

def list_tasks():
  os.system("clear")
  
  if len(tarefa) == 0:
    print("\nNenhuma tarefa adicionada!")
  else:
    print("\nLista de Tarefas:")
    for i in range(len(tarefa)):
      print(str(i+1) + ". " + tarefa[i])
      
def update_task():
  os.system("clear")
  
  if len(tarefa) == 0:
    print("\nNenhuma tarefa adicionada!")
  else:
    for i in range(len(tarefa)):
      print(str(i+1) + ". " + tarefa[i])
    index = input("\nEscolha a tarefa que deseja atualizar: \nSe quiser sair digite exit: ")

    if index != "exit":
      tarefa[int(index) - 1] = input("\nNova tarefa: ")
      print("\nTarefa atualizada!")
      return
    
    if index == "exit":
      return
    
def complete_task():
  os.system("clear")
  
  if len(tarefa) == 0:
    print("\nNenhuma tarefa adicionada!")
  else:
    for i in range(len(tarefa)):
      print(str(i+1) + ". " + tarefa[i])
    index = input("\nEscolha a tarefa que deseja marcar como concluída: \nSe quiser sair digite exit: ")

    if index != "exit":
      tarefa.pop(int(index) - 1)
      print("\nTarefa concluída!")
      return

    if index == "exit":
      return


def delete_task():
  os.system("clear")
  
  if len(tarefa) == 0:
    print("\nNenhuma tarefa adicionada!")
  else:
    for i in range(len(tarefa)):
      print(str(i+1) + ". " + tarefa[i])

    index = input("\nEscolha a tarefa que deseja excluir: \nSe quiser sair digite exit: ")
    
    if index != "exit":
      tarefa.pop(int(index) - 1)
      print("\nTarefa excluída!")
      return
      
    
    if index == "exit":
      return
    

while True:
  print("\nMenu do gerenciador de tarefas:")
  print("1. Adicionar tarefa")
  print("2. Listar tarefas")
  print("3. Atualizar tarefa")
  print("4. Completar tarefa")
  print("5. Excluir tarefa")
  print("6. Sair")

  option = input("Escolha uma opção: ")
  if option == "6":
    os.system("clear")
    
    print("\nSaindo...")
    break
  
  match option:
    case "1":
      add_task()
    case "2":
      list_tasks()
    case "3":
      update_task()
    case "4":
      complete_task()
    case "5":
      delete_task()