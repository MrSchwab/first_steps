import os.path

user_file_name = input("Please insert file name: ")
if os.path.isfile(user_file_name): #if it is a file = True

    while True:
        print("If you'd like to READ the file, type A")
        print("If you'd like to DELETE the current file and START OVER, type B")
        print("If you'd like to include new information in the file, type C")

        action = input("What would you like to do? ")
        print(action)

        #import pdb;pdb.set_trace()

        if action == "A" or action == "a":
            f = open(user_file_name, "r")
            print(f.read())
            f.close()

        elif action == "B" or action == "b":
            f = open(user_file_name, "w")
            user_info = input("Insert information: ")
            f.write(user_info)
            print(user_info)
            f.close()

        elif action == "C" or action == "c":
            f = open(user_file_name, "a")
            f.write("\n" + input("Insert information to be added to the file: "))
            f.close()

        elif action == "quit":
            break

        else:
            print("Invalid option, try again: ")

else:
    f = open(user_file_name, "w+")
    user_info = input("Insert information: ")
    f.write(user_info)
    print(user_info)
    f.close()
