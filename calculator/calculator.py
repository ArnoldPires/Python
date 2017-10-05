import re, math, sys, os
os.system('clear')

def help():
    print """Once you execute the calculator command, choose between a running the basic calculator or the scientific one.
    You can choose by either pressing 1 for basic or 2 for scientific!
"""
def basic():
    num1 = input("Type your first number and hit enter: ")
    num2 = input("Type your second number and hit enter: ")
    op = raw_input ("Select your Operator (+, -, *, /): ")
    equation = '%d %s %d' % (num1, op, num2)
    if op not in '+-*/':
        print "'" + op + "' is an invalid operator, please try again"
        basic()
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    else:
        result = num1 / num2
    print "And the answer is! '%s' is: %d" % (equation, result)

def scientific():
    global help
    global equation

    def eval_alpha():
        global equation
        return_list = []
        func = re.findall('((sin)(cos)|(tan)|(sqrt)) ([0-9\.]*)', equation)
        if not func:
            print "The function you specificed is not supported."
            help()
            sys.exit()
        for i in func:
            function = i[0] + " " + i[5]
            str = "math." + i[0] + "(" + i[5] + ")"
            return_list.append([function, eval(str)])
        return return_list

    def fact_check():
        global equation
        return_list = []
        func = re.findall('[0-9]*(?=!)', equation)
        for i in func:
            if i:
                    return_list.append([i + '!', math.factorial(int(i))])
            return return_list

        equation = raw_input("Enter your equation (type 'help' for help): ")

        while equation == "help":
            help()
            equation = raw_input("Enter your equation (type 'help' for help): ")

            orig_equation = equation
            equation = equation.replace('sine', 'sin')
            equation = equation.replace('costine', 'cos')
            equation = equation.replace('tangent', 'tan')

            equation = equation.replace ('pi', str(math.pi))

            equation = equation.replace('^', '**')

            equation = equation.replace('x','*')

            alpha = re.search('[a-zA-Z]', equation)
            if alpha:
                evaled = eval_alpha()
                for i in evaled:
                    equation = equation.replace(i[0], str(i[1]))

            fact + re.search('[0-9]*!', equation)
            if fact:
                fact_check = fact_check()
                for i in fact_checked:
                    equation = equation.replace(i[0], str(i[1]))

            result = eval(equation)
            if type(result) == int:
                print "The result of your equation '%s' is: %d" % (orig_equation, result)
            else:
                print "The result of your equation '%s' is: %.2f" % (orig_equation, result)

print """Choose a calculator
	1. Basic Calculator
	2. Scientific Calculator\n
    Type help() if you are confused
    """

choice = input(": ")

if choice == 1:
        basic()
elif choice == 2:
        scientific()
else:
    print "Invalid Choice"
