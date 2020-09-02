#print("Hello World")

#first_name = "Jason"
#print("Hello CSPT13 and" + first_name)
#print("Hello CSPT13 and", first_name)

#num = 23.87
#print(num)

#f string (string literals)
#print(f"This is a number ({1 +34})")

#strip removes whitespace from either end of the string
#my_string = "     this is a string       "
#print(my_string.strip())
#print(len(my_string)) 35
#print(len(my_string.strip())) 16

#print(f"Hello CSPT13 and           {len('this is a test')}       {first_name}.......".strip())
#print("Something on a new line")

#numbers = [1, 2, 3, 4, 5, 6]

#print(numbers)

#numbers.append(24)

#print(numbers)
#print(numbers[0])
#print(numbers[1])
#print(numbers[2])
#print(numbers[3])
#print(numbers[4])
#print(numbers[5])
#print(numbers[6])

#for number in numbers:
 #   print(number)


#for i in range(0,6):
#    print(numbers[i])

#for (i, e) in enumerate(numbers):
#    print(f"Element: {i} is {e}")

#i = 0
#while i < len(numbers):
#    print(numbers[i])
#    i += 1

#numbers = [1, 2, 3, 4]
#squares = [num * num for num in numbers]
    
#print(numbers)
#print(squares)

#evens = [num for num in numbers if num % 2 == 0]

#print(numbers)
#print(evens)


#names = ["Sarah", "jorge", "sam", "frank", "bob","sandy"]
#s_names = [name.capitalize() for name in names if name[0].lower() == 's']
#print(s_names)