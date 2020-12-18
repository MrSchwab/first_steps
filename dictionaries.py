# Sets

sets = {"element1","element2","element1","element4"}
print(sets)

if "element1" in sets:
    print("Yes")

# Countries

country_list = []
for i in range(5):
    country = input("Please enter your Country: ")
    country_list.append(country)

country_set = set(country_list)

print(country_list)
print(country_set)

if "Brazil" in country_set:
    print("Attended")

dictionary = {"key":"value","key2":"value2","key3":"value3"}

country_dictionary = {}

for country in country_list:
    if country in country_dictionary:
        country_dictionary[country] += 1

    else:
        country_dictionary[country] = 1

print(country_dictionary)


# Shoe store

black_shoes = {42:2,41:3,40:4,39:1,38:0}
print(black_shoes)

while(True):
    purchase_size = int(input("Which shoe size would you like to buy?\n"))
    if purchase_size < 0:
        break
    if black_shoes[purchase_size] > 0:
        black_shoes[purchase_size] -= 1
    else:
        print("Shoes are not available in this size.")
    print(black_shoes)

