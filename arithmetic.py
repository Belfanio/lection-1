def arithmetic(num1, num2, operation):
    num1 = float(input("Input first number: "))
    num2 = float(input ("Input second number: "))
    operation = str(input ("Input operation: "))
    if operation == "+":
        print (num1 + num2)
        
    elif operation == "-":
        print (num1 - num2)
        
    elif operation == "*":
        print (num1 * num2)
        
    elif operation == "/":
        print (num1 / num2)
        
    else: print ('unnown operation')