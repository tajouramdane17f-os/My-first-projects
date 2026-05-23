print ("Hello in simple calculator" \
"please enter the operation :" )
operation = input("enter the operation you want to perform (+, -, *, /): ")
evaluated_operation = eval(operation)
print("the result of the operation " + operation + " is: " + str(evaluated_operation))