# use build in functions to quickly leanr more about data

name = "Itumeleng"
height = 172.25
age = 34
employed = False

# Find out which datatype is stored in the 'name' variable
print()
name_datatype = type(name)
print(f"1. The data stored in 'name' variable is of type: {name_datatype}.")
print()

# Find more information about the 'name' variable and it's methods
available_methdds = dir(name)
space = ("\n" * 2)
print(f"2. Methods that belong to datatype {type(name)} are listed below: {space}{available_methdds}\n")

# # Select one method and find out how to use it
# selected_string_method = help(name.replace)
# print(selected_string_method)

# call the method and use it to manipulate the string
new_string = name.upper()
print(f"3. New string: {new_string}\n")

