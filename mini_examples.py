from question import Question
#MINI CALCULATOR
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = float (num1) + float (num2)
print(result)

#MADLIBS

color = input("Enter a color: ")
noun = input("Enter a plural noun: ")
name = input("Enter a name: ")


print("\nRoses are " + color)
print(noun + " are blue")
print("I love " + name)

#BETTER CALCULATOR

number1 = float(input("Enter first number: "))
operator = input("Enter operator: ")
number2 = float(input("Enter second number: "))

if operator == "+":
    print(number1 + number2)
elif operator == "-":
    print(number1 - number2)
elif operator == "*":
    print(number1 * number2)
elif operator == "/":
    print(number1 / number2)
else:
    print("You did not enter a valid operator.")

#GUESS THAT WORD

secret_word = "katze"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("\nYou lose :(")

else:
    print("\nYou win!")

#Exponent- Function


def raise_to_power(base_num, power_num):
    i = 0
    if power_num == 0:
        print(1)
        return

    result = 1
    while i < power_num:
        result = result * base_num
        i += 1
    print(result)

raise_to_power(10,2)
raise_to_power(10,0)
raise_to_power(3,3)

#Translator
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":

            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"

        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))

#Building Multiple Choice Quiz

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas\n(a) teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries\n(a) Yellow\n(b) Red\n(c) Blue\n\n"]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)
