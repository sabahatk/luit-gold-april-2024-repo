import sys

user_name = input("What is your name?")
if user_name == '':
    print("Empty name? I cannot work with that. I am closing the program. Bye!")
    sys.exit()
print("Hello,", user_name)
print("Let us get started...")

#While True:
#   print("Hi") #Example of KeyboardInterrupt

programming_languages = ["Java", "Python", "C++"]
print(programming_languages[10])

ages = {"Jim": 30, "Pam": 28, "Kevin": 33}
ages["Michael"]

age = input("What is your age? ")
print("In 10 years, you will be", age + 10)

age = int(input("What is your age? "))