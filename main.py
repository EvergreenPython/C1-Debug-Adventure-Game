print("Welcome to Calculator Program")

quit = input("If you want to quit press 'q' or to continue press any key: ")

while(quit != 'q'):

  print("What would you like to calculate?")
  print("(+) addition")
  print("(-) subtraction")
  print("(*) multiplication")
  print("(/) division")

  operators = input("Enter your choice: ")

  num1 = float(input("What is the first number? "))
  num2 = float(input("What is the second number? "))

  if(operators == "+" or operators == "addition"):
    print("You want to add")
    print(num1 + num2)
  elif(operators == "-" or operators == "subtraction"):
    print("You want to subtract")
    print(num1 - num2)
  elif(operators == "*" or operators == "muliplication"):
    print("You want to multiply")
    print(num1 * num2)
  elif(operators == "/" or operators == "division"):
    print("You want to divide")
    print(num1 / num2)
  else: 
    print("Invalid input")

  quit = input("If you want to quit press 'q' or to continue press any key: ")

print("Bye bye!")