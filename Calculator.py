num1 = int(input("Enter a Number"))
operator = input("Enter a Operator")
num2 = int(input("Enter a second Number"))
answer = 0

if (operator == "+") :
    answer = num1 + num2

elif (operator == "-") :
    answer = num1 - num2

elif (operator == "*") :
    answer = num1 * num2

elif (operator == "/") :
    answer = num1 / num2

elif (operator == "%") :
    answer = num1 % num2

else:
    answer ("Enter Valid Operator")

print(answer)
    
