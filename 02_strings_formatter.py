name = str(input("Enter your name: "))
age = int(input("Enter your age: "))

# print function using % method
print("Hi! My name is %s, and I am %d years old." %(name,age))

# print function using .format() with curly brace {}
print("Hi! My name is {0}, and I am {1} years old.".format(name, age))

# print function using f-string  with curly brace {}
print(f"Hi! My name is {name}, and I am {age} years old.")

