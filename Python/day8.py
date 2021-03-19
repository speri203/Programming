# Day 8 we are dealing with dictionaries. We are to create a phonebook and then be able
# to query this phonebook for a name and return the name=number.

# It seems as if the maps work the same way as a dictionary in Python.
# They are a way to store (key, value) data points that are stored into a datastructure.

# Link: https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem

phoneBook = {}
iteration = int(input())
for i in range(iteration):
    content = input().strip()
    content = content.split(" ")

    if content[0] not in phoneBook:
        phoneBook[content[0]] = content[1]

while True:
    try:
        inp = input()
        if inp in phoneBook:
            print(inp + "=" + phoneBook[inp])
        else:
            print("Not found")
    except EOFError:
        break
