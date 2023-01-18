# Do not modify these lines
__winc_id__ = '49bce82ef9cc475ca3146ee15b0259d0'
__human_name__ = 'functions'

# Add your code after this line

# greeting
def greet(name):
    return ("Hello, " + name + "!")
    
print(greet("Bob"))

# add three numbers
def add (a, b, c):
    return (a + b + c)

print (add (5, 3, 2))

# positive as boolean
def positive (y):
    if y > 0:
        return True
    else:
        return False

print (positive(50))
print (positive(-50))
print (positive(0))

# negative as boolean
def negative (x):
    if x < 0:
        return True
    else:
        return False

print (negative(50))
print (negative(-50))
print (negative(0))