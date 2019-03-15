# Nicholas Fahndrich
# 3/11/19
# FINAL PROJECT

name = input("What is your name: ")

print("Hi there " + name + "! " )
print("Welcome to the weight lifting calculator" + "\n")

while True:
    age = int(input("Enter Your age:"))
    if age > 100:
        print("You are too old to be lifting" + "\n")
    elif age < 14:
        print("You are too young to lift", "\n")
        break
    else:
        print("Thats the perfect age", "\n")
        break

while True:
    time_working = int(input("Enter how long you have been lifting:"))
    if time_working > 100:
        print("You are too old to be working out plain and simple" + "\n")
    elif time_working < 2:
        print("You should use this resource before adding more weight to your routine https://www.self.com/story/10-strength-training-tips-for-beginners-that-will-make-your-workout-more-effective", "\n")
        break
    else:
        print("Thats a good amount of years to be working out", "\n")
        break

print("Lets Get Your Maxes Recorded and Lets Total it")

for i in range(1):
    deadlift = int(input("What is your max deadlift: "))
    sum == deadlift

for i in range(1):
    squat = int(input("What is your max squat: "))
    sum = squat + deadlift

for i in range(1):
    bench = int(input("What is your max Bench: "))
    sum = squat + deadlift + bench
print("The total weight you have lifted is: " + str(sum)
      
def thanks_for_coming_to_my_program
      print 
