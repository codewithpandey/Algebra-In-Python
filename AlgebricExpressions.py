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
    result = expression
    # let's just take both operands first
    expRegex = re.compile(r'([0-9]?[a-zA-Z]\^?[0-9]?)\*([0-9]?[a-zA-Z]\^?[0-9]?)') # selects both co-efficients and variables.
    operands = expRegex.search(expression)
    operand1 = operands.group(1)
    operand2 = operands.group(2)
    # print(operand1, operand2)
    # let's check for the co-efficients if present
    op1Coef = ""
    op2Coef = ""
    for x in operand1:
        if x == "^":
            break
        if x.isnumeric():
            op1Coef += x
        else:
            pass
    for y in operand2:
        if y == "^":
            break
        if y.isnumeric():
            op2Coef += y
        else:
            pass
    # print (op1Coef, "*", op2Coef)

    if op1Coef == "":
        op1Coef = "1"
    if op2Coef == "":
        op2Coef = "1"

    resultCoef = str(int(op1Coef)*int(op2Coef))

    if "^" in operand1:
        expRegex = re.compile(r'(\^)([0-9])') # selects power of variable 1.
        power = expRegex.search(operand1)
        op1Power = power.group(2)
    else:
        op1Power = 1
    if "^" in operand2:
        expRegex = re.compile(r'(\^)([0-9])') # selects power of variable 2.
        power = expRegex.search(operand2)
        op2Power = power.group(2)
    else:
        op2Power = 1
    # print(op1Power, op2Power)

    var1 = ''.join(filter(str.isalpha, operand1))
    var2 = ''.join(filter(str.isalpha, operand2))

    if(var1 == var2):
        result = resultCoef + var1 + superScript(str(int(op1Power)+int(op2Power)))
    elif(var1 != var2):
        result = resultCoef + var1 + superScript(str(op1Power)) + var2 + superScript(str(op2Power))
    else:
        pass

    print(result)

# function to convert to superscript
def superScript(e):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    super_s = "ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾQᴿˢᵀᵁⱽᵂˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖ۹ʳˢᵗᵘᵛʷˣʸᶻ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾"
    res = e.maketrans(''.join(normal), ''.join(super_s))
    return e.translate(res)


# add("a+a")
# add("2a+3b")
# add("2a+3a")

mul("a^3*a^4")
mul("2a^2*3b^3")
mul("2a*3a")