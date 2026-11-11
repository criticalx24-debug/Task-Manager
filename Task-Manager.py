def add_tasks(tasks):
     task = input("\n Please Enter The Task: ")
     tasks.append(task)
     print("\n Task Added Successfully \n")
def view_tasks(tasks):
     if not tasks:
            print("\n No tasks found.\n")
     else:
            for number, task in enumerate(tasks):
                 print("\n" , number + 1 , task , "\n") 
def remove_tasks(tasks):
    try:
            if not tasks:
                print("\n The List is Empty. \n")
            else:
                sr = int(input("\n Enter Task Number: "))
                removed_task = tasks.pop(sr - 1)
                print("\n" , "Task:" , removed_task , "Removed Successfully \n")
    except IndexError:
                print("\n Please Choose From Existing Task Numbers \n")
    except ValueError:
                print("\n Please Choose a valid task number \n.")
def clear_tasks(tasks):
     if not tasks:
                 print("\n No tasks found To Be Removed \n.")
     else:
                 tasks.clear()
                 print("\n All Tasks Have Been Cleared \n.")
def edit_tasks(tasks):
     try:
           if not tasks:
               print("\n No Task Present To Be Edited \n")
           else:
               task_no = int(input("\n Enter Task Number: "))
               task = input("\n Please Enter The New Task: ")
               tasks[task_no - 1] = task
               print("\n Task Edited Successfully \n")
     except IndexError:
                print("\n Please Choose From Existing Task Numbers \n")
     except ValueError:
                print("\n Please Choose a valid task number. \n")
def save_tasks(tasks):
    with open("tasks.txt", "w") as file: 
        for task in tasks:
            file.write(task + "\n")
def load_tasks(tasks):
    try:
     with open("tasks.txt", "r") as file:
        for line in file:
            tasks.append(line.strip())
    except FileNotFoundError:
        pass
tasks = []
load_tasks(tasks)
while True:
    try:
        choice = int(input("What would you like to do? \n 1. Add a task \n 2. View Tasks \n 3. Remove a task \n 4. Clear all tasks \n 5. Edit a Task \n 6.. Exit The Program \n Please Enter Here ( 1/2/3/4/5/6 ):  "))
        if choice == 1:
          add_tasks(tasks)
          save_tasks(tasks)
        elif choice == 2:
          view_tasks(tasks)
        elif choice == 3:
          remove_tasks(tasks)
          save_tasks(tasks)
        elif choice == 4:
          clear_tasks(tasks)
          save_tasks(tasks)
        elif choice == 5:
           edit_tasks(tasks)
           save_tasks(tasks)
        elif choice == 6:
                print("Thanks for using the To-Do List!")
                break
          
        else:
            print("Choose From Options 1 - 6: ")
    except ValueError:
            print("Please Choose a valid option")
