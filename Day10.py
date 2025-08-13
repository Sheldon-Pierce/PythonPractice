
def format_name(f_name, l_name):
    """
    Take a first and last name and format it to return title case version of the name.
    """
    f_name = f_name.title()
    l_name = l_name.title()
    return f_name + " " + l_name

output = format_name('sheldon', 'pierce')
# print(output)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

def calculator ():
    should_continue = True
    number1 = int(input("Enter the first number: "))

    while should_continue:
        useroperation = input('Choose an operation: +, -, *, /')
        number2 = int(input("Enter the second number: "))
        result = operations[useroperation](number1, number2)
        print(f"{number1} + {number2} = {result}")
        userchoice = input("Would you like to continue with the previous result? Y or N").lower()
        if userchoice == 'y':
            number1 = result
        else:
            should_continue = False
            print("\n" * 20)
            calculator()

calculator()


