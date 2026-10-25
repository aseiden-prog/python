word = " "
total = 0
while word != "stop":
    word = input("how many pull-ups can you do? ")
    if word != "stop":
        number = int(word)
        total = total + number
print ("your total pull-ups:")
print (total)