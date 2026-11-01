age = (input("Enter your age: "))
money = (input("Enter how much money you have: "))
while age != "done" and money != "done":
    if int(age) >= 18 and int(money) >= 100:
        print("You can buy alcohol")
    if not int(age) >= 18 or not int(money) >= 100:
        print("get lost")
    age = (input("Enter your age: "))
    money = (input("Enter how much money you have: "))