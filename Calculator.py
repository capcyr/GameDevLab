numbers = int(input("What is your number"))
numbers2 = int(input("What is your other number"))
Operator = input("+,-,*,/")

if Operator == "+":
    result = numbers+numbers2 
    

elif Operator == "-":
      result = numbers-numbers2
      
elif Operator == "*":
      result = numbers*numbers2
      
elif Operator == "/":
      result = numbers/numbers2
print (result)