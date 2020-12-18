# Pirple Course - Homework 3

# Create a function that accepts 3 parameters and checks for equality between any two of them.

electricityOn = "yes"
alarm = "active"
safe = "yes"
alarmHoursOn = int("24")


if electricityOn == "yes" and alarm == "active":
    safe = "yes"

elif electricityOn != "yes" or alarm != "active":
    safe = "no"

if alarmHoursOn == 24:
    print("Perimeter secure all day long.")

if alarmHoursOn < 24:
    print("Perimeter not secure all day long.")

print("Is the perimeter secure?")
print(safe)
print("Alarm is on " + str(alarmHoursOn) + " hours a day.")
