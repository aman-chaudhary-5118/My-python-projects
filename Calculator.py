# process 1 : take input from the user
# input : numbers or operands like 1,2,3.. and operator like +,-,/,*
# input function use string by default so we have to change the data type
operand1 = input('please enter the first number - ')
operand2 = input('please enter the second number - ')
operator = input('enter the operator - ')

# change formats
# type conversion : changing the data type of one variable
operand1 = int(operand1)
operand2 = int(operand2)

# lets check the operator 
# we enter the operator in single commas because input function gives in string and we enter string in commas
# we add double equel to (==) or comparision operator because we want to check the operator 
if operator == '+':
  result = operand1 + operand1
elif operator == '-':
  result = operand1 - operand2
elif operator == '*':
  result = operand1 * operand2
elif operator == '/':
  result = operand1 / operand2
else :
  result = 'not defined'

print(result)