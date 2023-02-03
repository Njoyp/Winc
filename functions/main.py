# Do not modify these lines
__winc_id__ = '49bce82ef9cc475ca3146ee15b0259d0'
__human_name__ = 'functions'

# Add your code after this line

# greeting, greet: takes a name and returns a string
def greet(name):
    return ("Hello, " + name + "!")
    
print(greet("Bob"))

# add three numbers, add: takes three numbers (integers or floats) and returns their sum
def add (a, b, c):
    return (a + b + c)

print (add (5, 3, 2))

# positive as boolean, positive: takes a number (integer or float) and returns whether or not it is positive in the form of a boolean. You do not have to handle the case where the argument is not an int or a float.
def positive (y):
    if y > 0:
        return True
    else:
        return False

print (positive(50))
print (positive(-50))
print (positive(0))

# negative as boolean, takes a number (integer or float) and returns whether or not it is negative in the form of a boolean. You do not have to handle the case where the argument is not an int or float.
def negative (x):
    if x < 0:
        return True
    else:
        return False

print (negative(50))
print (negative(-50))
print (negative(0))