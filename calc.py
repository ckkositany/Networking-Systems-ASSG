operand=input("Enter the type of operation (+ - * /): ")
num1=float( input("Enter the first number: "))
num2=float( input("Enter the second number: "))

if operand =="+":
    result=num1 + num2
    print(round(result,3))
elif operand=="-":
    result=num1 - num2
    print(round(result,3))
elif operand=="*":
    result=num1 * num2
    print(round(result,3))
elif operand=="/":
 result=num1 / num2
 print(round(result,3))

else:
 print(f"{operand} Is not a valid operand")

