# Pirple Course
# Participant Data

participant_number = 2
participant_data = []
registered_participants = 0
output_file = open("participant_data.txt","w")

while(registered_participants < participant_number):
    temp_part_data = [] #name, country, age

    name = input("Please enter your name: ")
    temp_part_data.append(name)

    country = input("Please enter your country of origin: ")
    temp_part_data.append(country)

    age = int(input("Please enter your age: "))
    temp_part_data.append(age)
    print(temp_part_data)

    participant_data.append(temp_part_data)
    print(participant_data)

    registered_participants += 1

for participant in participant_data:
    for data in participant:
        output_file.write(str(data))
        output_file.write(" ")

    output_file.write("\n")

output_file.close()

input_file = open("participant_data.txt","r")

input_list = []

for line in input_file:
    temp_participant = line.strip("\n").split()
    print(temp_participant)
    input_list.append(temp_participant)
    print(input_list)

age = {}
for part in input_list:
    temp_age = int(part[-1])
    if temp_age in age:
        age[temp_age] += 1
    else:
        age[temp_age] = 1

print(age)

oldest = 0
youngest = 100
most_freq_age = 0
counter = 0

for temp_age in age:
    if temp_age > oldest:
        oldest = temp_age
    if temp_age < youngest:
        youngest = temp_age
    if age[temp_age] >= counter:
        counter = age[temp_age]
        most_freq_age = temp_age

print("The oldest participant is:",oldest)
print("The youngest participant is:",youngest)
print("Most occurring age is:",most_freq_age,"with",counter,"participants.")

input_file.close()
