# Nicholas Fahndrich
# 3/11/19
# FINAL PROJECT

name = input("What is your name: ")

print("Hi there " + name + "! " )
print("Welcome to the weight calculator" + "\n")

while True:
    age = int(input("Enter your age:"))
    if age > 100:
        print("You are too old to be lifting" + "\n")
    elif age < 14:
        print("You are too young to lift", "\n")
        break
    else:
        print("Thats the perfect age to be lifting", "\n")
        break

