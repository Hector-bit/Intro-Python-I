"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"

print("x is %d, y is %f, z is %s" % (x, y, z))

# Use the 'format' string method to print the same thing

txt = "x is {num1}, y is {num2}, z is {str}"
print(txt.format(num1 = x, num2 = y, str = z))

# Finally, print the same thing using an f-string

txt2 = f"x is {x}, y is {y}, z is {z}"
print(txt2)