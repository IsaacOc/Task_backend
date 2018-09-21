from task import todo_list, create_task ,delete_task, mark_as_finished, delete_all_tasks # import other functions as well
from account import login, add_account  # import the function as well


if __name__ == "__main__":
    """
        Allow a person to input a name and a password

        E.g
    """
    name = input("Enter your name: ")
    password = input("Enter your password: ")

    """
        Let the person sign in. If there details do not exist,
        create an account for them

        E.g 
    """
    #add_account("brian", "ndela35$$")
    add_account(password,name)
    print(login(password,name))


    """
        Provide options:
            1. creating a task
            2. deleting a task 
            3. deleting all tasks
            4. Marking a task finished

        E.g
    """

    print("Select Option:")
    print("1: Create Task")
    print("2: delete Task")
    print("3: Marking a task finished")
    print("4: delete all Task")

# ..... skipped code
    selection = input("selection: ")

#Write code that implements the selected option

"""
The above should appear as
    Select Options:
        1. Create Task
        2 .... 
        3 ....
        4 ....

    selection:
"""
if selection == "1":
    name = input("Enter your task: ")
    create_task(name)
    selection = input("selection: ")

if selection == "2":
    name = input("Enter your task to delete: ")
    delete_task(name)
    selection = input("selection: ")

if selection == "3":
    name = input("Enter your task to mark as finished: ")
    mark_as_finished("."+name)
    selection = input("selection: ")

if selection == "4":
     name = input("Are you sure to delete all task: yes or no")
     if name == "yes":
         delete_all_tasks()
         selection = input("selection: ")
     else:
         pass