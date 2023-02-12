# variables
listing = []
i = 0


while True:
    work = input("Enter 0 for skip. Work: ")
    if work != str(0):
        if work != "":
            listing.append([len(listing) + 1, work , False])
            print("Your ToDo list is updated ")
            if i >= 1:
                task = input("""What do you want to do next?
                        Press Enter key to continue adding items.
                        Edit: To edit the list.
                        Print: To print the ToDo list
                        Exit: To exit the program
                        \n-> """)
                
                # For editing 
                if task.lower() == "edit":
                    a = int(input("""
                        1. To edit Task.
                        2. To edit completion.
                        3. To exit edit mode.
                        
                        Enter the command from one of the above(Only the number):  """))
                    # 1. To edit Task.
                    if a == 1:
                        for i in range(0, len(listing)):
                            print(listing[i][0], ". ", listing[i][1], " \t| ", listing[i][2])
                        taskNumberA = int(input("Enter Work No. : "))
                        taskNumberA -= 1
                        if taskNumberA <= len(listing):
                            newTask = input("Enter 0 to cancel. Enter new task: ")
                            if newTask != str(0):
                                listing[taskNumberA][1] = newTask
                            else:
                                pass
                    # 2. To edit completion.
                    elif a == 2:
                        taskNumberB = int(input("Enter Work No. : "))
                        taskNumberB -= 1
                        if taskNumberB <= len(listing):
                            TrueOrFalse =  input("Enter 'True' or 'False': ")
                            if TrueOrFalse == True or TrueOrFalse == False:
                                listing[taskNumberB][2] = TrueOrFalse
                            else:
                                print("Invalied Term! ")
                        else:
                            print("Invalied Work No.! ")
                    # 3. To exit edit mode
                    elif a == 3:
                        pass
                    # No valied 
                    else:
                        print("Invalied Task! ")
                # For printing the ToDo list
                if task.lower() == "print":
                    for i in range(0, len(listing)):
                        print(listing[i][0], ". ", listing[i][1], " | ", listing[i][2])
                # For exit program
                if task.lower() == "exit":
                    exit()
            else:
                i = i + 1
                continue
        else: print("Item must not empty!")
        
    


for i in listing:
    print(i)
