import useful_tools
from student import Student
from Chef import Chef
from FrenchChef import FrenchChef

#PRINT FUNCTION

print("Hello World")

print("    /|")
print("   / |")
print("  /  |")
print(" /___|")

#VARIABLES

character_name = "Cyprien"
character_food = "pizza"
character_situation = "broken"
per_day = "20"

print(character_name + " loves to eat.")
print(character_name +" eats about " + per_day + " " + character_food + " each day.")
print("if " + character_name + " continues to eat so much " + character_food + ", he will probably end up getting " + character_situation)

#WORKING WITH STRINGS

print("Hi, how's it going? \n")
print("Hi,\n I'm just dandy? \n")
print("\"just dandy\" huh")

phrase = "yoooooooooo" #STRING VARIABLES
print("\n" + phrase + " what are thoseeeee?? \n")

upper_case = "COWS ARE CUTE"
lower_case = upper_case.lower()
print(upper_case + " " + lower_case + " " + lower_case.upper() + "\n")

print(upper_case.isupper())
print(upper_case.islower())
print(upper_case.lower().islower())
print(len(upper_case))
print('\n')

print(upper_case[0])
index_4_C = upper_case.index("C")
print(index_4_C)
print(upper_case[index_4_C])

print(upper_case.index("cute".upper()))
print("\n")
print(upper_case.replace("COWS", "DUCKS"))

#WORKING WITH NUMBERS

print(2)
print(2.01243)
print(-2.012)
print((3+3) * 5)
print(10 % 3)

my_num = 5
print(my_num)

print(str(my_num) + " cups of coffee")

neg_num = -10
print(abs(neg_num))

print(pow(2,15))
print(max(10,11))
print(min(10,11))
print(round(5.52))
print(round(5.5))

from math import *
print(floor(3.7))
print(ceil(3.8))
print(sqrt(64))

#INPUT FROM A USER

name = input("Enter your name: ")
surname = input("Enter your surname")
print("hi " + name + " " + surname)

#LISTS

friends = ['Ryan', 'Max', 'Jimmy', 'Lorenzo', 'Cole']
types = ["friends", 2, False]

print(friends)
print(friends[0])
print(friends[-2])
print(friends[2:])
print(friends[2:4])

friends[1] = "John"
print(friends)

#LIST FUNCTIONS

friends.extend(types)
print(friends)

friends.append("Jeff")
print(friends)

friends.insert(2,"Blake Homon")
print(friends)

friends.remove("John")
print(friends)

types.clear()
print(types)

friends.pop()

print(friends.index("Jimmy"))

print(friends.count("Jimmy"))

odd_num = [17,25,5,9,157,123,15]
odd_num.sort()
print(odd_num)

odd_num.reverse()
print(odd_num)

odd_copy = odd_num.copy()
odd_copy.append(77)
odd_copy.sort()
print(odd_copy)

#TUPLES

coordinate = (4, 5)
print(coordinate[0])
coordinates = [(4, 5), (6, 7), (80, 34)]

#FUNCTIONS

def sayhi():
    print("Hello user")

sayhi()

def print_input():
    word = input("Enter a word to print: ")
    print(word)

print_input()

def age(num):
    print("you are " + num + " years old")

my_age = input("how old are you? ")

age(my_age)

#return statements
def cubed(num):
    return num*num*num

print(cubed(3))
twenty_seven = cubed(3)

#IF-STATEMENTS

am_awake = True
am_hungry = False
is_raining = False

if am_awake:
    print("Good Moring")
    if am_hungry:
        print("Breakfast timeeee")
    else:
        print("Breakfast later")

    if is_raining:
        print("Good idea to bring umbrella")
    else:
        print("ouuu, the sun is out")
else:
    print("Shhhh he/she is sleeping")



if am_hungry and am_awake:
    print("Good moring, would you like some waffles?")

elif am_awake:
    print("Would you like to eat later?")

else:
    print("Shhhh he/she is sleeping")

if am_awake and not(is_raining):
    print("let's go for a run")

#IF-STATEMENTS AND COMPARISONS

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1

    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(5,8,15))

#DICTIONARIES

monthConversations = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversations["Nov"])
print(monthConversations.get("Dec"))
print(monthConversations.get("Meme", "Not a valid key"))

#WHILE-LOOPS

i = 1
while i <= 10:
    print("I have " + str(i) + " cats")
    i+=1


#FOR-LOOPS

for letter in "Cats are cool":
    print(letter)

cats = ["Toby", "Chester", "Garfield", "Moe"]
for name in cats:
    print(name)

for index in range(0, 11):
    print(index)

for index in range(len(cats)):
    print(cats[index])

#2D Lists & Nested Loops

number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [9]
]

print(number_grid[0][0])
print(number_grid[1][2])

for row in number_grid:
    for col in row:
        print([col])

#Try-Except
try:
    number = int(input("Enter a number: "))
    print(number)
except ValueError as err:
    print(err)

#READING FILES

food_file = open("foods.txt", "r")
#print(food_file.readlines()[0])
for food in food_file.readlines():
    print(food)
food_file.close()

#Writing and appending to a file
food_file = open("foods.txt", "a") #Appending

food_file.write("\nRamen - Japonese")
food_file.close()

food_file = open("foods1.txt", "w") #Writing a new file
food_file.write("\nRamen - Japanese")
food_file.close()

#Module and Pipes

print(useful_tools.roll_dice(10))

#Classes and Objects

student1 = Student("Cyp", "CS", 3.77, False)
print(student1.gpa)

#Object functions
print(student1.on_honor_roll())

myChef = Chef()
myChef.make_tofu()
myChef.make_special_dish()

#inheritance
myFrenchChef = FrenchChef()
myFrenchChef.make_special_dish()
myFrenchChef.make_chocolate_mouse()