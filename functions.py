import math

## opens a file in read mode
## filename received as a parameter
def openFile(filename):
    try:
        infile = open(filename, "r")

        print("File opened.")
    except FileNotFoundError:
        raise FileNotFoundError("File does not exist")
    except:
        raise TypeError("Filename type can not be openned")

## takes two numbers and returns
## the result of a division
def numbers(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        raise ZeroDivisionError("Divisor can not be zero.")
    except:
        raise TypeError

## takes in two points
## finds the distance between the points
def dist(x1, y1, x2, y2):
    dist = (x2 - x1) ** 2 + (y2 - y1) ** 2
    dist = math.sqrt(dist)

    return dist

## takes in a string -- reverses it
## then compares the two
def isPalindrome(temp):
    if type(temp) != str:
        raise TypeError("Word must be a string.")
    temp = temp.lower()
    test = temp[::-1]

    if(test == temp):
        return True

    else:
        return False

## has input to receive two numbers
## divides the two, then outputs the result
def divide():
    try:
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
    except:
        raise TypeError("Input must be numbers.")
    if num2 == 0:
        raise ZeroDivisionError

    div = num1 / num2

    print("Your numbers divided is:", div)

## returns the squareroot of a particular number
def sq(num):
    if num < 0:
        raise ValueError("Number can not be less than zero.")
        
    return math.sqrt(num)

## grabs user's name
## greets them by their entire name
## names should be strings
def greetUser(first, middle, last):
    if (type(first) != str or type(middle) != str or type(last) != str):
        raise TypeError("Name must be a string.")
    if (not first.isalpha() or not middle.isalpha() or not last.isalpha()):
        raise ValueError("Name contains non alpha characters.")
    
    print("Hello!")
    print("Welcome to the program", first, middle, last)
    print("Glad to have you!")

## takes in a Python list
## attempts to display the item at the index provided
def displayItem(numbers, index):
    if type(numbers) == list:
        print("Your item at", index, "index is", numbers[index])
    else:
        raise TypeError(f'Numbers must be a list, not {type(numbers)}')
