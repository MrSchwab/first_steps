# Pirple Course - Homework 7
# Dictionaries and Sets

song_input = input("What's your favorite song? ")
singer_input = input("Who sings it? ")
album_input = input("What is the name of the album it was launched in? ")
genre_input = input("What kind of music is that? ")
released_input = input("What year was it released in? ")
recorded_input = input("When was it recorded? ")
length_input = input("How long is the song? ")

songs = {"song":song_input, "singer":singer_input, "album":album_input, "genre":genre_input, "released":released_input, "recoded":recorded_input, "length":length_input}

for key, value in songs.items():
    print(key+":"+value)

print(songs)
