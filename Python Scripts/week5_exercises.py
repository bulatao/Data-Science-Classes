import random



def better_guess_number():
    x=0
    secret_number = random.randint(1,10)
    while x < 3:
        guess = int(input("guess a number between 1 and 10:"))
        if guess == secret_number:
            print("you got it")
            break
        if guess < secret_number:
            print("too low")
        if guess > secret_number:
            print("too high")
        x += 1
    if x >=3:
        print("you lose")

def login():
    x = 0
    user = input("Please enter your user name:")
    if user == "admin":
        while x <3:
            password = input("Please enter your password:")
            if password == "password":
                print("Welcome aboard, admin")
                break
            if password !="password":
                print("Wrong password, try again")
            x+=1
        if x>=3:
            print("too many wrong attempts.")
    else :
        print("Welcome guest!")


def right_alignment(n):
    for x in range(1,n):
        print((" "* (100-(2*x)))," *"*x)
        
    
