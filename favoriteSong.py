# Homework 1 - Pirple Course

# Make a file called main.py containing information about your favourite song.

song = "My Way"

singer = "Frank Sinatra"
"""there are many different versions, 
with many different singers. 
My favourite one is Elvis Presley."""

album = "\"My Way\""
genre = "Traditional Pop"
released = 1969
recorded = 1968 # It was recorded in Los Angeles
lengthInMinutes = 4.5
writer1 = "Claude François" 
writer2 = "Jacques Revaux"

print("My favourite song is " + song + ".")
print("It is best known in the voice of " + singer + ".")
print("It was released in an album called " + album + ".")
print("It was classified as " + genre + ".")
print("It was released in " + str(released) + ".")
print("It was recorded in the year " + str(recorded) + ".")
print("It is " + str(lengthInMinutes) + " minutes long.")
print("It was written by " + writer1 + ", " + writer2 + ".")

# string format (%i = integer) // (%f = float) // %.3d
