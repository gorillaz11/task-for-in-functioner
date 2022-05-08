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
        index=int(input("enter task swap position!!:"))-1

        def swapPositions(tasks, pos1, pos2):
            first_ele=tasks.pop(pos1)
            second_ele=tasks.pop(pos2-1)
            tasks.insert(pos1, second_ele) 
            tasks.insert(pos2, first_ele) 
            index=pos1,pos2
            pos1=int(input("input position 1"))-1
            pos2=int(input("input position 2"))-1

            tasks[index]=new_tasks

            return tasks
            
    if option==0:
        break     