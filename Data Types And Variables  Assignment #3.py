#1 Declare two variables, num1 and num2, with any integer values. Use these to calculate their sum and print the result
num1 = 1
num2 = 5
sum = num1 + num2
print("the sum of num1 and num2 is:", sum)

#2 Create a variable called message and give it a string value. Append the string " World!" to it and print the updated message.
message = "Hello"
print(message)
message += " World"
print(message)

#3 Declare a variable, is_python_fun, and assign it a boolean value. Print a statement based on whether Python is considered fun. 
is_python_fun = True

if is_python_fun:
    print("Python is considered fun!")
else:
    print("Python is not considered fun.")

#4 Create a list called fruits with at least three different fruit names. Print the list, add a new fruit, and then print the updated list.
fruits = ["apple","mango","orange"]
type(fruits)
fruits.append("banana")
print(fruits)

#5 Declare a variable called price with a floating-point value. Convert it to an integer and print both the original and converted values.
price = float(50.0)
print(price)
integer = int(price)
print(integer)

#6 Create a dictionary named student_info with keys for 'name', 'age', and 'grade'. Assign corresponding values and print the dictionary.
student_info = {"name" : "Ali Abdullah","age" : "14","grade" : "9th"}
type(student_info)
print(student_info)

#7 Create a complex number variable, comp_num, with real and imaginary parts. Print both parts separately.
comp_num = 3 + 4j 
complex_no = complex(comp_num)
Real = complex_no.real
Imaginary = complex_no.imag
print("Real part of your complex number is:",Real)
print("Imaginary part of your complex number is:",Imaginary)

#8 Write a program that takes user input for their age and prints a message addressing their age group (e.g., "Teenager," "Adult").
age = int(input("Enter your age:"))
if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")             

#9 Combine two strings using concatenation. Use string interpolation to include the length of the resulting string in a print statement.
string1 = "Hello"
string2 = " Ali Abdullah"
combined_strings = string1 + string2
print( combined_strings)
length = len(combined_strings)
print("the length of the combined string is:", length)

#10 Create a tuple named days_of_week with the names of the days. Access and print the third day of the week.
days_of_week = ("monday","tuesday","wednesday","thursday","friday","saterday","sunday")
type(days_of_week)
print(days_of_week[2])