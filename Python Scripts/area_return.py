def area_return(width,length):
    
    ''' comment out all sorts o fstuff
on multiple linse
on other stuff
close out with triple single quotes
'''
    return width*length

def area_print(width,length):
    print (width*length)
    # something is commented here
    return

def getName():
    #this is the function header
    name = input("Please enter your name:\n")
    print("Hello", name)

def getName2(name):
    print("Hello ", name)

def greetings():
    name = input("Enter the name")
    times = input("How many times to repeat the name?")
    times = int(times)
    print(name*times)

def F2C(farenheit):
    celcius = (farenheit - 32) * 5 / 9
    return celcius

def C2F(celcius):
    farenheit = (celcius * 9 / 5) + 32
    return farenheit

def madlib():
    name = input("give me a name: ")
    action = input("what action do you want to do: ")
    place = input("give me a place: ")
    print("%s is %s at %s" %(name,action,place))

def myprojects():
    madlib()
    name = input("name sucker")
    getName2(name)

def maderlib(name, action, place):
    #name = input("give me a name: ")
    #action = input("what action do you want to do: ")
    #place = input("give me a place: ")
    print("%s is %s at %s" %(name,action,place))


def right_justify(stringA):
    s = 70 - len(stringA)
    print(" "*s+stringA)

    
    
