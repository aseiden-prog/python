choice = ""
while choice != "stop":
    choice = input("Pick a verb: + - * / or stop ")
    if choice != "stop":
        first = int(input("First number: "))
        second = int(input("Second number: "))
        if choice == "+":
            print(first + second)
        elif choice == "-":
            print(first - second)
        elif choice == "*":
            print(first * second)
        elif choice == "/":
            if second != 0:
                print(first / second)
            else:
                print("Cannot divide by zero")
        else:
            print("I don't know that verb")
print("done")
