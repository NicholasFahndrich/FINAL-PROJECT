'''
Nicholas Fahndrich
3/11/19
What we have here is a program that will add you maxes together
'''
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

while True:
    time_working = int(input("Enter how long you have been lifting:"))
    if time_working > 100:
        print("You are too old to be working out" + "\n")
    elif time_working < 2:
        print("You should use this resource before working out https://www.self.com/story/10-strength-training-tips-for-beginners-that-will-make-your-workout-more-effective", "\n")
        break
    else:
        print("Thats the perfect amount of years to be working out", "\n")
        break

print("Lets Get Your Maxes Recorded and Lets Total it")

for i in range(1):
    deadlift = int(input("What is your max deadlift: "))
    sum == deadlift

for i in range(1):
    squat = int(input("What is your max squat: "))
    sum = squat + deadlift

print("The total of your numbers is: " + str(sum))

'''
We have a program that asks people for their names. It then asks for their age. It will tell you if you are a good age to be lifting or not
it asks how long you have been lifting and if you say below 2 it gives you a resource to get some more info on weight lifting. The program gathers your maxes and will add them all
up and will tell you how mucg weight you have lifted total
'''