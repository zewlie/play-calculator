def add(arg_list):
    sum = 0
    for num in arg_list:
        addend = int(num)
        sum += addend

    return sum

def subtract(arg_list):
    difference = 0
    for index, num in enumerate(arg_list):
        subtractend = int(arg_list[index])
        difference -= subtractend

    return difference

def multiply(arg_list):
    product = 1
    for index in range(0,len(arg_list)):
        factor = int(arg_list[index])
        product *= factor

    return product

def divide(arg_list):
    quotient = arg_list[0]
    for num in arg_list[1:]:
        divisor = float(arg_list[index])
        quotient /= divisor
        print "q= " , quotient

    return quotient

def square(arg_list):
    num1 = int(arg_list[0])

    return num1 ** 2

def cube(arg_list):
    num1 = int(arg_list[0])

    return num1 ** 3

def power(arg_list):
    result = arg_list.pop(1)
    for num in arg_list:
        exponent = float(num)
        result = result ** exponent

    return result

def mod(arg_list):
    result = int(arg_list[0])
    for index in range(1,len(arg_list)):
        modulus = int(arg_list[index])
        result = result % modulus

    return result


