# Let's solve algebra using python programs.
# In an algebric expression we don not have a numeric value which can be calculated.
# So we have to do evry step that we do in our copies.
# For example normally by multiplication we mean to multiply two values. But as for in algbra we have to perform a concatination operation.
# i.e. a * b = ab
# for division we will leave as it is i.e. a/b

import re


def add(expression):
    result = expression
    # let's just take bothe operands first
    expRegex = re.compile(r'([0-9]?[a-zA-Z])\+([0-9]?[a-zA-Z])') # selects both coeefficients and variables.
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
    
    # selecting only the variables
    var1 = ''.join(filter(str.isalpha, operand1))
    var2 = ''.join(filter(str.isalpha, operand2))

    if(var1 == var2):
        result = str(int(op1Coef)+int(op2Coef))+var1
    else:
        pass


    # print(var1, var2)
    

    print(result)


add("2a+3b")
add("2a+3a")