# Homework 6 - Pirple Course
# Advanced Loops

length = 10
to_print = "a"

for pos in range(1,length+1):
    print(to_print*pos)

for pos in range(length-1,0,-1):
    print(to_print*pos)



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
#        print(" | | ")
    else:
        print(19*"-")

x = 2
for i in range(x):
      for j in range(x):
            a = x -  j + i
            print(a)
