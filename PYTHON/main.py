#Starting the journey of the Python

#In python we doesn't have to declare the variable, it itself defined or will know its its data types

#This is a single line comment 
"""
This is multiline comment
"""

#First program to print your name or the most famous dialogue in Programming terms
print("Hello! World")
print("Hi, I am ___________")
#In the line you can print your name

#Lets jump into the Coding


#Program to take input from user and print that 
ask=input("Enter anything you like: ")
print("You have entered: ",ask)

#This program adds two numbers
num1=int(input("Enter 1st number: "))
num2=int(input("Enter 2nd number: "))

#Add two numbers 
sum = num1 + num2

#Display the sum 
print("The sum of {0} and {1} is {2}".format(num1,num2,sum))
#You can choose between any arithmetic opertaion in this format , you just have to switch in between the signs

"""For addition: +
For subtraction: -
For multiplication: *
For division: /
"""

#Program for the arithmetic operations

num1=int(input("Enter 1st number: "))
num2=int(input("Enter 2nd number: "))

sum=num1+num2
difference=num1-num2
product=num1*num2
division=num1/num2
modulo=num1%num2
exponent= num1**num2
floor_division=num1//num2


print("The sum of {0} and {1} is {2}".format(num1,num2,sum))
print("The difference of {0} and {1} is {2}".format(num1,num2,difference))
print("The product of {0} and {1} is {2}".format(num1,num2,product))
print("The division of {0} and {1} is {2}".format(num1,num2,division))
print("The modulus of {0} and {1} is {2}".format(num1,num2,modulo))
print("The exponentiation of {0} and {1} is {2}".format(num1,num2,exponent))
print("The floor_division of {0} and {1} is {2}".format(num1,num2,floor_division))

#Program for the comparison operator

The comparison operator includes: 
Equals to: ==
Not equals to: !=
Greater than: >
Less than: <
Greater than or equal to: >=
Less than or equal to: <=

num1=int(input("Enter 1st number: "))
num2=int(input("Enter 2nd number: "))

if(num1==num2):
    print("Both entered numbers are equal.")
    
elif(num1!=num2):
    print("Entered numbers are not equal.")
    
if(num1>num2):
    print("{0} is greater than {1}".format(num1,num2))
elif(num1<num2):
    print("{1} is greater than {0}".format(num2,num1))
    
if(num1>=num2):
    print("{0} is greater than or equals to {1}". format(num1,num2))
elif(num1<=num2):
    print("{1} is greater than or equals to {0}". format(num2,num1))
# (. dot) is used to end the program 
