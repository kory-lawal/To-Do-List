import sys
todo_list = []

while True:
  try:
    print("""1.Add to list\n2.TO do list\n3.exit""")
    OPT = int(input("Enter your choice: "))

    if OPT== 1:
      #option 1: ADD to-do list
      task = input("Enter to add task: \n")
      todo_list.append(task)
      print("task added to list.\n")

    elif OPT == 2:
      #option 2: Display to-do list
      if not todo_list:
        print("The to-do list is empty\n")
      else:
        print("To-Do List/n")
        for i, task in enumerate(todo_list, start=1):
          print(f"{i}. {task}")

    elif OPT == 3:
      #option 3: Exit the program
      print("Exiting the program")
      sys.exit()

    else:
         print("Invalid choice. Please enter a valid option (1, 2, or 3).")

  except ValueError:
        print("Invalid input. Please enter a number (1, 2, or 3).")




  


    



