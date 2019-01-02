'''create a functino called compare numbers, which takes two numerical parameters
 compares them and print out if one is larger than the otehr
 (number, number) -> print a string
 ex: compare_numbers(5,10)
 "5 is less than 10"
 '''

def compare_number(x,y):
    if x>y:
        print(x, " is greater than ", y)
    if x<y:
        print(y,  " is greater than ",  x)
    else:
        print(x,  " is equal to ", y)


def is_even(x):
    if x%2==0:
        print(x, " is an even number")
    else:
        print(x, " is an odd number")

''' create a function called retire_or_not
this function prompts user to enter age
define a variable called retirement_age
then compare the user entered age with retirement age
if user age is greater or equal to retirement age
then print "you can retire and relax now!"
otherwise print, you can retire in " xxx years
'''

def retire_or_not():
    retirement_age = 65
    age = input("How old are you?")
    age=int(age)
    if age >= retirement_age:
        print("you can retire and relax now!")
    else:
        print("you can retire in ", retirement_age - age, " years.")

def check_grade(x):
    if x >= 90:
        print("letter grade:A")
    if x >=80 and x < 90:
        print("leter grade:B")
    if x >=70 and x <80:
        print("letter grade:C")
    if x >=60 and x<70:
        print("letter grade:D")
    if x <60:
        print("letter grade:F")

def grading():
    x = int(input("what numeric grade did you get for class 1? "))
    check_grade(x)
    y = int(input("what numeric grade did you get for class 2? "))
    check_grade(y)
    z = int(input("what numeric grade did you get for class 3? "))
    check_grade(z)

import random

def number_guess():
    counter = 0
    while counter <3:
        secret_number = random.randint(1,10)
        guess = int(input("guess a number between 1 and 10 "))
        if guess == secret_number:
            print("you guessed the right number")
        else:
            print("wrong, the number was %d" %secret_number)
        counter += 1
