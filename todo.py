from turtle import clear


tasks =[]
while True:
    print("!.menu")
    print("1.add task")
    print("2.explain task")
    print("3.remove task")
    print("4.change task")
    print("5.swap task")
    option=int(input(">>>>"))
    if option== 1:
        while True:
            new_tasks = input("Name your new tasks:")
            if new_tasks =="":
                break
            if new_tasks not in tasks:
                tasks.append(new_tasks)




    if option==2:
        print("Your tasks:")

        for i in range(len(tasks)):
            print(i+1,">",tasks[i])
        
        input("\nhit any key to continue")
    if option==3:
        index=int(input("enter task position!!:"))-1
        for index in  tasks:
                tasks.remove(index)


    if option==4:


        index=int(input("enter task position!!:"))-1
        new_tasks=input("enter new tasks title!!:")
        tasks[index]=new_tasks
    if option == 5:
        pos1=int(input("first position:"))
        pos2=int(input("second position:"))
        tasks[pos2],tasks[pos1]=tasks[pos1],tasks[pos2]
    if option==0:
        break     