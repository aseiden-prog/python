grocery = []
list = (input("Enter an item "))
while list != "done":
    grocery.append(list)
    list = (input("Enter another item "))
for item in grocery:
    print (item)
print(len(grocery))
print(grocery[len(grocery)-2])