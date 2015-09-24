"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

#dictionary mapping operands to functions in arithmetic.py
command_dic = {"+":add, "-":subtract, "*":multiply, "/":divide,
                "square":square, "cube":cube, "pow":power, "mod":mod}

while True:
    #get input from user
    input_string = raw_input(">")

    #tokenize user input (first arg is operator, rest are arguments)
    tokens = input_string.split()

    #get just the arguments
    args = tokens[1:]

    #quit if requested to do so
    if tokens[0] == "q" or tokens[0] == "Q":
        break

    #otherwise, look up given operator and run corresponding function
    print command_dic[tokens[0]](args)



