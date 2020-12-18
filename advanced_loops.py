for row in range(21):
    if row%2 == 0:
        for column in range(1,20):
            if column%2 == 1:
                if column != 19:
                    print(" ",end="")
                else:
                    print(" ")
            else:
                print("|",end="")
    else:
        print(19*"-")
