# I/O

#scores = []
#
#for i in range(5):
#    current_score = float(input("Please enter the score "+str(i+1)+": "))
#    scores.append(current_score)
#    print("The score you entered was:",current_score)
#
#print(scores)


# Creating a File

#file = open("Filename","r") #"r", "w", "a", "r+" --> read and write
#file.close()

vacation_spots = ["London","Paris","New York","Utah","Iceland"]

vacation_file = open("vacation_places","w")

for spots in vacation_spots:
    vacation_file.write(str(spots + "\n"))

vacation_file.close()

vacation_file = open("vacation_places","r")

first_line =  vacation_file.readline()
print(first_line)
second_line = vacation_file.readline()
print(second_line)
for line in vacation_file:
    print(line, end = "")

the_whole_file = vacation_file.read()

print(the_whole_file)

vacation_file.close()

final_spot = "Thailand\n"

vacation_file = open("vacation_places","a")
vacation_file.write(final_spot)
vacation_file.close()

vacation_file = open("vacation_places","r")
for line in vacation_file:
    print(line, end = "")

vacation_file.close()

for i in range(5):
    with open("vacation_places"+str(i),"r") as vacation_file:
        for line in vacation_file:
            print(line)
