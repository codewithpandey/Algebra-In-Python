import re


def add(expression):
    result = expression
    # let's just take both operands first
    expRegex = re.compile(r'([0-9]?[a-zA-Z])\+([0-9]?[a-zA-Z])') # selects both co-efficients and variables.
    operands = expRegex.search(expression)
    operand1 = operands.group(1)
    operand2 = operands.group(2)
    # let's check for the co-efficients if present
    op1Coef = ""
    op2Coef = ""
    for x in operand1:
        if x.isnumeric():
            op1Coef += x
        else:
            pass
    for y in operand2:
        if y.isnumeric():
            op2Coef += y
        else:
            pass
    # print (op1Coef, "+", op2Coef)
    if op1Coef == "":
        op1Coef = "1"
    if op2Coef == "":
        op2Coef = "1"
    # selecting only the variables
    var1 = ''.join(filter(str.isalpha, operand1))
    var2 = ''.join(filter(str.isalpha, operand2))
    
    if(var1 == var2):
        result = str(int(op1Coef)+int(op2Coef))+var1
    else:
        pass


    # print(var1, var2)
    

    print(result)

def mul(expression):
    pass



add("a+a")
add("2a+3b")
add("2a+3a")