todo_list = []

def create_task(task):

    """ Adds the task (string value) to todo_list """
    todo_list.append(task)
    print("--Adding item to todo list")
    print(todo_list)
    print("-----")

def delete_task(task):
    """ Remove the specified task from the todo_list """
    print("--Removeing item--")
    todo_list.remove(task)
    print(todo_list)
    print("-----")

def mark_as_finished(task):
    """
    Append the string label '[finished]' at the end of the task 
    if it does not already have the label appended.
    It should remain in the todo_list
    """
    for i in range(todo_list.__len__()):
        
        if todo_list[i].__contains__(task):
            print(todo_list[i])
            print("-----")
        else:
            print("--marking finished---")
            print(todo_list[i].__add__(task))
            todo_list.insert(i,todo_list[i].__add__(task))
            print("-----")

def delete_all_tasks():
    """
    Empty the the todo_list
    """
    #del todo_list[:] deletes too
    print("list deleted")
    todo_list.clear()
    print(todo_list)



#create_task("Eat")
#create_task("paly")
#mark_as_finished(".[finished]")
#delete_task("paly")
#create_task("play")
#delete_all_tasks()

