grocery = []
list = (input("Enter an item "))
while list != "done":
    grocery.append(list)
    list = (input("Enter another item "))
for item in grocery:
    print (item)
