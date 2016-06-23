#!/usr/bin/env python3
import cgi
import html

form = cgi.FieldStorage()

num_1 = float(form.getfirst("num1"))
num_2 = float(form.getfirst("num2")) 
operation = form.getfirst("operation")

def add (num_1, num_2):
	return num_1 + num_2
def substract (num_1, num_2):
	return num_1 - num_2
def multiply (num_1, num_2):
	return num_1 * num_2
def divide (num_1, num_2):
    if num_2 == 0:
        return "Wrong operation. Cannot divide by 0"
        quit()
    else:
        return (num_1/num_2)
    
calc = {'add': add, 'substract': substract, 'multiply': multiply, 'divide': divide}
result=calc[operation](num_1, num_2)

print("Content-type: text/html\n")

print ("<h2>Result is</h2>")
print ("<p>{}</p>".format(result))

"""the program executes basic calculation operations such as adding, 
substruction, multiplication and division of two numbers.
program gets two input numbers and selected operation from form index.html, processes get values and returns result of calculation. there is set a max. allowed floating step of 0.01 for input"""
