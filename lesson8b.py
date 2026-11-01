first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
choice = input("pick a verb + - * / ")
if choice == "+":
    print(first + second)
elif choice == "-":
    print(first - second)
elif choice == "*":
    print(first * second)
elif choice == "/":
    print(first / second)
else:
    print("i don't know that verb")