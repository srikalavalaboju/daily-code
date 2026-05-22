#TO-DO LIST
tasks = []
while True:
    print("_____TO DO LIST_____")
    print("1.Add Task Into List")
    print("2.View Tasks From  List")
    print("3.Remove Task From List")
    print("4.Exit")
    choice = input("Enter your choice:")
    if choice == "1" :
        task = input("Enter Your Task:")
        tasks.append(task)
        print("Task is added successfully to List") 
    elif choice == "2":
        if len(tasks) == "0":
            print("List is Empty,No Task is available")
        else :
            print("Your Tasks :")
            count = 1
            for task in tasks:
                print(count,".",task)
                count = count + 1
    elif choice == "3" :
        if len(task) == "0":
            print("There is no tasks to remove")
        else:
            print("your Task")
            count = 1
            for task in tasks :
                print(count,".",task)
                count = count + 1
            num = int(input("Enter task number to remove:"))
            if num > 0 and num <= len(tasks) :
                print(tasks.pop(num-1),"removed from list successfully")
            else:
                print("Invalid task ")
    elif choice == "4" :
            print("Exit")
            break
    else :
        print("Invalid choice")
