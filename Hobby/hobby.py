friend1 = set(input("Enter first friends hobby ").split(','))
friend2 = set(input("Enter second friends hobby ").split(','))

friend1 = {hobby.strip() for hobby in friend1}
friend2 = {hobby.strip() for hobby in friend2}

commonhobbies = friend1 & friend2
if commonhobbies:
    print (commonhobbies)
else:
    print("There are no common hobbies")
