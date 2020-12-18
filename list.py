# Homework 4 - Pirple Course

# Lists

myUniqueList = []
print(myUniqueList)
myLeftovers = []
print(myLeftovers)

def addToList(element):

    if element not in myUniqueList:
        element = myUniqueList.append(element)
        return True

    elif element in myUniqueList:
        element = myLeftovers.append(element)
        return False

addToList(1)
print(myUniqueList)
print(myLeftovers)

addToList(1)
print(myUniqueList)
print(myLeftovers)

addToList(2)
print(myUniqueList)
print(myLeftovers)
