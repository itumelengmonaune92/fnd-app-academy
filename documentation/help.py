# use build in functions to quickly leanr more about data

name = "Itumeleng"
height = 172.25
# age = 34
# employed = False

# Task:1
# Find out which datatype is stored in the 'name' variable
print()
name_datatype = type(name)
print(f"1. The data stored in 'name' variable is of type: {name_datatype}.")
print()

# Find more information about the 'name' variable and it's methods
available_methods1 = dir(name)
space = ("\n" * 2)
print(f"2. Methods that belong to datatype {type(name)} are listed below: {space}{available_methods1}\n")

# # Select one method and find out how to use it
# selected_string_method = help(name.replace)
# print(selected_string_method)

# call the method and use it to manipulate the data
new_string = name.upper()
print(f"3. New string: {new_string}\n")

# Task:2
# Find out which datatype is stored in the 'height' variable
print()
height_datatype = type(height)
print(f"4. The data stored in 'height' variable is of type: {height_datatype}.")
print()

# Find more information about the 'height' variable and it's methods
available_methods2 = dir(height)
space = ("\n" * 2)
print(f"5. Methods that belong to datatype {type(height)} are listed below: {space}{available_methods2}\n")

# # Select one method and find out how to use it
# selected_float_method = help(height.is_integer)
# print(selected_float_method)

# call the method and use it to manipulate the data
equation = 100 / height
result = equation.is_integer() # checks if the data store in the variable is an integer and return True or False
print(f"6. The total value/quotient pf the equation is an integer (True/False): {result}\n")


