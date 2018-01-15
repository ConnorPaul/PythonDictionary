classes = open("courses2.txt", "r")

classdictionary = {}

for line in classes:
    line = line.strip()
    parts = line.split()
    if parts[0] in classdictionary:
        classdictionary[parts[0]].append(parts[1])
    else:
        a = []
        a.append(parts[1])
        classdictionary[parts[0]] = a
print(classdictionary)

#Prints out the numbers of all courses in the dictionary.
print("Question 1:")
for n in classdictionary:
    print(n)
print("-------")

#Prints out the names of all of the instructors.
print("Question 2:")
print(classdictionary.values())
print("-------")

#Prints out all of the instructors who have taught 523.
print("Question 3:")
print(classdictionary.get('523'))
print("-------")

#Prints out the courses taught by instructor Capra.
print("Question 4:")
for (k,v) in classdictionary.items():
    if "Capra" in v:
        print(k)
